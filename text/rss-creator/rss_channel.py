class RssChannel:
  """
    Defines RSS Channel attributes
  """
  def __init__(self, title: str,
               description: str,
               link: str,
               language: str,
               copyright_notice: str,
               managing_editor: str,
               web_master: str,
               pub_date: str,
               last_build_date: str,
               category: str,
               generator: str,
               docs: str,
               cloud: str,
               ttl: str,
               image: str,
               rating: int,
               text_input: str,
               skip_hour: str,
               skip_days: str) -> None:
    self.title = title
    self.description = description
    self.link = link
    self.language = language
    self.copyright_notice = copyright_notice
    self.managing_editor = managing_editor
    self.web_master = web_master
    self.pub_date = pub_date
    self.last_build_date = last_build_date
    self.category = category
    self.generator = generator
    self.docs = docs
    self.cloud = cloud
    self.ttl = ttl
    self.image = image
    self.rating = rating
    self.text_input = text_input
    self.skip_hour = skip_hour
    self.skip_days = skip_days
  