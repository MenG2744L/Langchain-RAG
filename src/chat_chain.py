from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import QianfanChatEndpoint
from langchain.prompts import ChatPromptTemplate
from langchain_core.language_models.chat_models import HumanMessage

load_dotenv("E:\\python-prj\\Langchain-RAG\\.env")

template_string = """不改变意思文本原意 \
that is delimited by triple backticks \
改写为反AI工具不容易识别的样式 \
文本: ```{text}```
"""
prompt_template = ChatPromptTemplate.from_template(template_string)

customer_email = """
地面防空部队应当坚定不移地推进一体化联合侦察预警体系的建设，以显著提升空中侦察预警的效率。通过综合运用雷达、光学、红外以及人工侦察等多种手段，构建全面而精细的对地综合侦察部署，实现对不同类型无人机的精确探测。
应对日益复杂的无人机威胁，地面防空部队必须专注于研发专业的反无人机技术装备。借鉴如瑞典“长颈鹿”系列雷达和美国国防部高级研究计划局“天网”等最新技术，我们的系统能够大幅提升无人机的探测、识别和跟踪能力。这套系统具备探测超过100个空中目标的能力，即便是RCS不小于0.001m的微小型无人机，也能在300米以下的高度进行长时间的有效监视。
我们必须高度重视地面综合观察哨网络的建设。在无人机可能渗透的关键区域，优先部署观察哨所，并结合便携式防空导弹形成“哨弹组合”的防御模式，以实现对无人机威胁的快速反应和有效拦截。
为了拓展空中侦察方式，我们将采用预警机、空中侦察气球、预警飞艇等多种手段，构建多维度的预警体系。其中，特别要关注专门用于探测和识别敌方无人机的无人预警机的发展，这将极大地丰富我们的空中反无人机侦察手段。
构建一体化联合空中情报信息网络也是我们的重要工作之一。通过全军空中情报联网和军民综合空中情报联网，我们将实现空中情报信息的实时共享，为地面防空部队提供更加准确、及时的情报支持，从而全面提升防空作战的效能。

"""

customer_messages = prompt_template.format_messages(
    text=customer_email)

chat = QianfanChatEndpoint(
    streaming=True,
    model="ERNIE-Bot-turbo"
)
print(chat.invoke(customer_messages).content)

# def get_completion(prompt, model="ERNIE-Bot"):
#     messages = [
#         {"role": "user",
#          "content": prompt}
#     ]
#     qianfan_chat = QianfanChatEndpoint(
#         streaming=True,
#         messages=messages,
#         model=model,
#         temperature=0.5,
#     )
#     return qianfan_chat.invoke(messages).content
#
#
# print(get_completion(customer_messages))
