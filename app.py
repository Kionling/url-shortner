from flask import Flask, request, redirect, render_template, url_for
import sqlite3
import random
import string

app = Flask(__name__)


def get_random_string(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))


def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS urls (short TEXT, original TEXT)')
    conn.commit()
    conn.close()
