# 产品名称
PageTemper（暂定名）

# 使用场景
## 接入
- 微信号运营者角度

  1. 如果现在已经有后台程序，将现有的微信服务号的App ID和App secret发给PageTemper，以及在后台程序部分添加一小段代码用于把用户访问文章的行为传给PageTemper（各种语言的后台都可以，内容就是openID和对应文章的URL，由当前使用的后台负责获取用户访问文章的行为）
  2. 如果没有对接后台，我们可以提供完完整功能的后台服务器
  3. PageTemper提供一个Dashboard账号给服务号运营者

## 被动回复
- 微信号运营者角度（仅限尚无后台的情况）
  1. 在微信的后台撰写文章
  2. 在PageTemper的后台点击刷新获得新编辑的文章，勾选当前要被动回复的文章（可多选）
  3. （可选）服务号推送提示文字“今日有新内容，回复xx阅读全文”给用户
  4. 当接受到用户发送的某些消息时自动回复之前选择的文章列表（图文形式）

- 用户角度
  1. （可选）接收到服务号发送的“今日有新内容，回复xx阅读全文”类文字
  2. 回复xx给服务号，获得图文形式的文章列表
  3. 用户点击任何文章都会被记录下来

## 主动推送文字
- 微信号运营者角度
  1. 在微信的后台撰写文章
  2. 在PageTemper的后台点击刷新获得新编辑的文章
  3. 在PageTemper中选择要推送的文章
  4. 自动生成要推送的标题＋链接的文字内容，可二次编辑
  5. 文字内容主动推送给用户

- 用户角度
 1. 用户收到“标题＋链接的文字内容”类的文字推送
 2. 点击文章链接查看微信文章页面

## 主动推送图文
- 微信号运营者角度
 1. 在微信的后台撰写文章
 2. 在PageTemper的后台点击刷新获得新编辑的文章
 3. 在PageTemper中选择要推送的文章
 4. 图文形式的推送发给用户
 5. 引导用户点击阅读原文
 6. 用户点击阅读原文后，即可统计访问

- 用户角度
 1. 接收到图文推送
 2. 点击进入文章，点击查看原文
 3. 如果没有关注过这个服务号的用户会跳转到授权页面，关注过后就不再显示授权页面
 4. 查看文章的原文页面

## 用户标签
- 微信号运营者角度
 - 在PageTemper的后台查看所有用户的Tag情况

## 用户定向信息推送
- 微信号运营者角度
 1. 在PageTemper的后台点选需要推送的用户群（按Tag划分）
 2. 选择推送的形式（主动文字或图文）

- 用户角度
 - 与前面的效果一致

## 注意事项
- 订阅号的分析需要借助第三方账号才可以实现网页授权，记录行为，但无法按Tag向用户推送信息
- 被动回复的形式则不需要授权即可完成记录