import requests
import logging
import os

logger = logging.getLogger("SpellClassesREST")

base_url = os.environ.get('API_SPELLS_CLASSES_URL')

def lista_spell():
    return __get(base_url + 'listaSpell/')


def lista_spell_por_classe(classe):
    return __get(base_url + 'listaSpell/' + classe)


def lista_classe():
    return __get(base_url + 'listaClasse/')


def spell_especifico(spell):
    return __get(base_url + 'spell/' + spell)


def __get(url):
    logger.info('Fazendo a chamada do endpoint - ' + url)

    try:
        response = requests.get(url).json()
    except Exception as e:
        response = "Ocorreu um erro inexperado"
        logger.info(e)

    logger.info('Resposta - ' + response)

    return response
