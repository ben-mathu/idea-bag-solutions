from pathlib import Path
import sqlite3
import os

class SqliteDatabase:
  
  def __init__(self, db_name):
    if ".db" != "".join(db_name[:-3]):
      db_name += ".db"
    
    if not os.path.exists(os.path.dirname("temp/" + db_name)):
      path = Path(os.path.dirname(db_name))
      path.parent.mkdir(exist_ok=True, parents=True)
    self.connection = sqlite3.connect(db_name)
  
  def close(self):
    self.connection.close()