from unittest.mock import MagicMock, Mock
from main.common.sqlite_handler import SqliteDatabase
import unittest
import sqlite3
import pytest


@pytest.fixture(scope="function")
def connection(request):
  sqlite3.connect = MagicMock(return_value=request.param)
  db = SqliteDatabase(db_name="var/test_database")
  return db

def test_sqlite_class_called():
  sqlite3.connect = MagicMock(return_value='request.param')
  db = SqliteDatabase(db_name="var/test_database")
  sqlite3.connect.assert_called_with("var/test_database.db")

@pytest.mark.parametrize("connection", [("connection succeeded")])
def test_sqlite_connect_success(connection):
  assert connection == "connection succeeded"

@pytest.mark.parametrize("connection", [("connection failed")])
def test_sqlite_connect_fail(connection):
  assert connection == "connection failed"