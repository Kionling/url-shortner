from flask import Flask, request, redirect, render_template, url_for
import sqlite3
import random
import string

app = Flask(__name__)


def get_random_string(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))