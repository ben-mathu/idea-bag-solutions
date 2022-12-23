class RssItem:
  """
    Cass to hold channel element Item
  """
  def __init__(self, title: str,
               link: str,
               description: str,
               author: str,
               category: str,
               comments: str,
               enclosure: str,
               guid: str,
               pub_date: str,
               source: str) -> None:
    self.title = title
    self.link = link
    self.description = description
    self.author = author
    self.category = category
    self.comments = comments
    self.enclosure = enclosure
    self.guid = guid
    self.pub_date = pub_date
    self.source = source