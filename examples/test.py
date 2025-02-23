from qwen_agent.agents import Assistant
from qwen_agent.gui import WebUI

llm_cfg = {
    'model': 'qwen2.5:3b',
    'model_server': 'http://127.0.0.1:11434/v1/',  # base_url, also known as api_base
    'api_key': 'EMPTY',
}

def app_gui():
    # Define the agent
    bot = Assistant(llm=llm_cfg,
                    name='Assistant',
                    description='使用RAG检索并回答，支持文件类型：PDF/Word/PPT/TXT/HTML。')
    chatbot_config = {
        'prompt.suggestions': [
            {
                'text': '如何办理保险？'
            },
            {
                'text': '如何理赔？'
            },
        ]
    }
    WebUI(bot, chatbot_config=chatbot_config).run()


if __name__ == '__main__':
    app_gui()