from flask import Flask, jsonify, request, abort
import json


def bad_request(message):
    response = jsonify({'error': message})
    response.status_code = 400
    return response

def not_found(message):
    response = jsonify({'error': message})
    response.status_code = 404
    return response

def write_json(path, data):
    with open(path, 'w+') as outfile:
        json.dump(data, outfile)

def read_json(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid