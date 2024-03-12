from telegram import Bot, Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filtersfrom telegram import Bot, Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# 替换为你的机器人API token
TOKEN = 'YOUR_BOT_TOKEN'
# 替换为你希望机器人管理的群组ID
GROUP_ID = 'YOUR_GROUP_ID'
# 替换为你希望发送给新成员的消息
WELCOME_MESSAGE = "欢迎加入我们的群组！请阅读群组规则并完成要求后，回复此消息获取密码。"

# 初始化机器人
bot = Bot(TOKEN)
updater = Updater(TOKEN, use_context=True)

# 检测新成员加入群组的功能
def new_member(update, context):
    # 检查是否是加入群组的事件
    if update.message.new_chat_members:
        # 遍历新加入的成员
        for member in update.message.new_chat_members:
            # 向每个新成员发送欢迎信息
            bot.send_message(chat_id=member.id, text=WELCOME_MESSAGE)

# 设置消息处理器
new_member_handler = MessageHandler(Filters.status_update.new_chat_members, new_member)
updater.dispatcher.add_handler(new_member_handler)

# 开始监听
updater.start_polling()

# 运行直到按下Ctrl-C或程序被终止
updater.idle()
