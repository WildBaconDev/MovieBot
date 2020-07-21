import logging
import json
import spells_classes_ded

logger = logging.getLogger('Actions')


def action_handler(action, parameters, return_var):
    return_values = {}

    if action == "listagem_spells_por_classe":
        return_values = get_listagem_spells_por_classe(parameters, return_var)
    elif action == "spell_especifico":
        return_values = get_spell_especifico(parameters, return_var)
    elif action == "listagem_spells":
        return_values = get_listagem_spells(return_var)
    elif action == "listagem_classes":
        return_values = get_listagem_classe(return_var)

    logger.info('return_values' + json.dumps(return_values))

    return {
        'skills': {
            'main skill': {
                'user_defined': return_values
            }
        }
    }


def get_listagem_spells(return_var):
    logger.info("get_listagem_spells")

    result = spells_classes_ded.lista_spell()

    logger.info("get_listagem_spells - retorno - " + result)

    return __construir_retorno(return_var, result)


def get_spell_especifico(parameters, return_var):
    logger.info("get_spell_especifico - Parametros - " + json.dumps(parameters))

    result = spells_classes_ded.spell_especifico(parameters['spell_especifico'])

    logger.info("get_spell_especifico - retorno - " + result)

    return __construir_retorno(return_var, result)


def get_listagem_classe(return_var):
    logger.info("get_listagem_classe - Parametros")

    result = spells_classes_ded.lista_classe()

    logger.info("get_listagem_classe - retorno - " + result)

    return __construir_retorno(return_var, result)


def get_listagem_spells_por_classe(parameters, return_var):
    logger.info("get_listagem_spells_por_classe - Parametros - " + json.dumps(parameters))

    result = spells_classes_ded.lista_spell_por_classe(parameters['classe'])

    logger.info("get_listagem_spells_por_classe - retorno - " + result)

    return __construir_retorno(return_var, result)


def __construir_retorno(return_var, result):
    return {return_var: result}
