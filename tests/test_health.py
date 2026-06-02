# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_health.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: luluzuri <luluzuri@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/03 00:17:01 by luluzuri          #+#    #+#              #
#    Updated: 2026/06/03 00:31:44 by luluzuri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

url = "/"

def test_root_return_200(client):
    response = client.get(url)
    assert response.status_code == 200

def test_root_returns_json(client):
    response = client.get(url)
    assert response.json() == {"message": "hello world"}

def test_openapi_is_available(client):
    r = client.get("/openapi.json")

    assert r is not None
