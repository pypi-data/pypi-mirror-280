import json
from docarray import BaseDoc, DocList
from typing import Dict, Optional, Literal, List
import srsly
from pydantic import Field, validate_arguments

class Message(BaseDoc):
    role: Literal['user', 'assistant', 'system'] = Field(description="message角色, 必须是['user', 'assistant', 'system']中的一个")
    content: str = Field(description="message内容", default=None)
    
    
class MessageFromTemplate(Message):
    """通过模版和参数来format content，主要可以确保修改message模版后的旧数据依然可用
    """
    template: str = Field(description="message模版，其中的参数通过kwargs来填充，便于修改模板后重新构建message", default=None)
    kwargs: Dict[str, str] = Field(description="message 参数，便于修改模板后重新构建message", default=None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.template is not None and self.kwargs is not None:
            self.content = self.template.format(**self.kwargs)
        else:
            raise ValueError("必须提供template和kwargs")
        
    
class DialogueDoc(BaseDoc):
    """存放openai格式的对话历史
    """
    system: Optional[str] = None
    system_message: Message = None
    conversation: DocList[Message] = DocList[Message]()
    theme: Optional[str] = None
    situation: Optional[str] = None
    tags: List[str] = []
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.system is not None and self.system_message is None:
            self.system_message = Message(role="system", content=self.system)
    
    @property
    def messages(self):
        list = []
        # 兼容旧数据中system
        if self.system is not None and self.system_message is None:
            self.system_message = Message(role="system", content=self.system)
        if self.system_message is not None:
            list.append(self.system_message)
        list.extend(self.conversation)
        return list
    
    
    
class DialogueDocList(DocList[DialogueDoc]):
    
    @classmethod
    def from_instruction_jsonl(cls, jsonl_path: str) -> "DialogueDocList":
        """json格式需要为instruction, input, output, history
        注意:
        - history的格式应为[{'role': 'user', 'content': 'hello'}, {'role': 'assistant', 'content': 'hello'}].
        - role只能为user或者assistant.
        """
        docs = DialogueDocList()
        for line in srsly.read_jsonl(jsonl_path):
            doc = DialogueDoc(system=line['instruction'])
            if line['history']:
                for his in line['history']:
                    doc.conversation.append(Message(role=his['role'], content=his['content']))
                
            input_message = Message(role='user', content=line['input'])
            output_message = Message(role='assistant', content=str(line['output']))
            doc.conversation.append(input_message)
            doc.conversation.append(output_message)
            docs.append(doc)
        return docs
    
    def to_instruction_jsonl(self, jsonl_path, **dump_kwargs) -> None:
        """转换为instruction jsonl数据格式

        Args:
            jsonl_path (str): 保存的jsonl文件
        """
        with open(jsonl_path, "w", encoding="utf-8") as fo:
            for d in self:
                input_message = d.conversation[-2]
                output_message = d.conversation[-1]
                line = {"instruction": d.system}
                
                if len(d.conversation) <= 2:
                    line['history'] = []
                else:
                    for m in d.conversation[:-2]:
                        line['history'].append({"role": m.role, "content": m.content})
                line['input'] = {"role": input_message.role, "content": input_message.content}
                line['output'] = {"role": output_message.role, "content": output_message.content}
                fo.write(json.dumps(line, **dump_kwargs)+"\n")
        
        
    
    @classmethod
    def from_qwen_jsonl(cls, jsonl_path:str) -> "DialogueDocList":
        """从千问的jsonl数据格式导入doc

        Args:
            jsonl_path (str): qwen jsonl文件
        """
        docs = DialogueDocList()
        for line in srsly.read_jsonl(jsonl_path):
            source = line['source']
            doc = DialogueDoc(id=source)
            doc.tags.append(source.split("-")[1])
            for m in line['messages']:
                if m['role'] == 'system':
                    doc.system = m['content']
                else:
                    doc.conversation.append(Message(role=m['role'], content=m['content']))
            docs.append(doc)
        return docs
    
    def to_qwen_jsonl(self, jsonl_path:str, **dump_kwargs) -> None:
        """转换为千问的jsonl数据格式

        Args:
            jsonl_path (str): 保存的jsonl文件
            dump_kwargs: json dump参数
        """
        with open(jsonl_path, "w", encoding="utf-8") as fo:
            for d in self:
                line = {"type": "chatml", "source": d.id, "messages":[]}
                messages = d.messages
                line['messages'] = [{"role":m.role, "content":m.content} for m in messages]
                fo.write(json.dumps(line, **dump_kwargs)+"\n")
    
    @validate_arguments
    def quick_add(self, conversation: List[str], system: str = None, theme: str = None, situation: str = None):
        """快速添加对话,默认user在前,assistant在后,且交替出现
        """
        doc = DialogueDoc(system=system, theme=theme, situation=situation)
        for i, message in enumerate(conversation):
            if i % 2 == 0:
                doc.conversation.append(Message(role='user', content=message))
            else:
                doc.conversation.append(Message(role='assistant', content=message))
        self.append(doc)                    
        

class FunctionCall(BaseDoc):
    name: str = Field(description="函数名称")
    arguments :str = Field(description="函数参数，JSON格式")

class FunctionCallMessage(Message):
    function_call: FunctionCall = Field(description="选择的Function及其输入参数")

class FunctionCallProperty(BaseDoc):
    type: str = Field("参数类型，如int，string等")
    description: str = Field("参数描述")

class FunctionCallParameters(BaseDoc):
    properties: Dict[str, FunctionCallProperty] = Field(description="参数字典，key为参数名称，value为其类型，描述")
    required: List[str] = Field(description="必须的参数名称，必须是properties中的key")
    
class FunctionCallDescription(BaseDoc):
    name: str = Field(description="函数名称")
    description: str = Field(description="函数描述")
    parameters: FunctionCallParameters

class FucntionCallDialogueDoc(DialogueDoc):
    functions: List[FunctionCallDescription]
    
class FucntionCallDialogueDocList(DocList[FucntionCallDialogueDoc]):
    pass