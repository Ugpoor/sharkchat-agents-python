from agents import Agent, Runner
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel  # 导入模型包装类

# 1. 使用转发站地址初始化客户端
forwarder_client = AsyncOpenAI(
    api_key="",  # 转发站的认证密钥，需要自行填入
    base_url="https://apihw.sharkchat.cn/v1"  # 转发站地址
)

# 2. 创建建模型实例，绑定客户端
custom_model = OpenAIChatCompletionsModel(
    model="gpt-3.5-turbo",  # 模型名称（根据转发站支持的模型填写）
    openai_client=forwarder_client  # 传入转发站客户端
)

# 3. 创建 agent 时指定模型
agent = Agent(
    name="历史学家",
    instructions="根据真实情况回答",
    model=custom_model  # 绑定配置好的模型
)

# 运行 agent
result = Runner.run_sync(agent, "请告诉我周树人和鲁迅是否同一个人？")
print(result.final_output)