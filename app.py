# Custom imports 
from multipage import MultiPage
from pages import cls_zt, sentiment

# Create an instance of the app 
app = MultiPage()


app.add_page("市场原始数据",sentiment.app)
app.add_page("财联社涨停分析",cls_zt.app)
# The main app
app.run()
