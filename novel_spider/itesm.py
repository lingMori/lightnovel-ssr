from scrapy import Field
import scrapy


class NovelItem(scrapy.Item):
    title = Field()
    author = Field()
    cover_url = Field()
    cover_local_path = Field()

    # content
    description = Field()
    content = Field()
    tags = Field()
    genre = Field()

    # metadata
    source_site = Field()
    source_url = Field()
    publish_date = Field()
    update_date = Field()
    crawl_date = Field()

    # status
    status = Field()  # e.g., ongoing, completed
    word_count = Field()  # List of chapter items
    chapter_count = Field()  # Total number of chapters

     # 评价信息
    rating = Field()                # 评分
    view_count = Field()            # 阅读量
    favorite_count = Field()        # 收藏数

     # 扩展字段
    extra_data = Field()            # 额外数据
