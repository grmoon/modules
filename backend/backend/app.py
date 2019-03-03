import asyncio
import json
import logging
import websockets
import traceback

from enum import Enum, auto

from available_modules import AVAILABLE_MODULES, MODULES_BY_TYPE

logger = logging.getLogger(__name__)
connections = {}

class Command(Enum):
    CALCULATE = 'calculate'
    GET_AVAILABLE_MODULES = 'get_available_modules'

def serialize_module(module):
    inputs = module.get_input_types()
    outputs = module.get_output_types()

    return {
        'inputs': {key: value.__name__ for key, value in inputs.items()},
        'type': module.__name__,
        'outputs': {key: value.__name__ for key, value in outputs.items()},
    }

async def get_available_modules(websocket):
    content = [serialize_module(module) for module in AVAILABLE_MODULES]

    response = {
        'command': Command.GET_AVAILABLE_MODULES.value,
        'content': content
    }

    await websocket.send(json.dumps(response))


async def build_inputs(module_inputs, outputs):
    inputs = {}
    can_calculate = True

    for input_name, module_input in module_inputs.items():
        input_source = module_input['source']

        if input_source == 'constant':
            inputs[input_name] = module_input['value']
        elif input_source in outputs:
            source_input_name = module_input['value']
            inputs[input_name] = outputs[input_source][source_input_name]
        else:
            can_calculate = False
            break

    return inputs, can_calculate

async def calculate(websocket, modules):
    outputs = {}

    current_modules = {}
    next_modules = modules
    prev_current_models_len = len(current_modules.keys())
    all_calculated = True
    calculation_occurred = True

    while next_modules and calculation_occurred:
        calculation_occurred = False
        current_modules = next_modules
        next_modules = {}

        for module_id, module in current_modules.items():
            module_class = MODULES_BY_TYPE[module['type']]
            inputs, can_calculate = await build_inputs(module['inputs'], outputs)

            if can_calculate:
                calculation_occurred = True

                await websocket.send(json.dumps({
                    'command': 'module_calculation_started',
                    'content': {
                        'module_id': module_id
                    }
                }))

                try:
                    outputs[module_id] = module_class.run(inputs)
                except Exception as exc:
                    await websocket.send(json.dumps({
                        'command': 'module_calculation_error',
                        'content': {
                            'module_id': module_id
                        }
                    }))
                else:
                    await websocket.send(json.dumps({
                        'command': 'module_calculation_finished',
                        'content': {
                            'module_id': module_id
                        }
                    }))
            else:
                next_modules[module_id] = module

    await websocket.send(json.dumps({
        'command': 'calculations',
        'content': {
            'completed': all_calculated,
            'outputs': outputs,
        }
    }))

async def consumer(websocket):
    while True:
        try:
            message = json.loads(await websocket.recv())
            command = message['command']

            if command == Command.GET_AVAILABLE_MODULES.value:
                await get_available_modules(websocket)
            elif command == Command.CALCULATE.value:
                await calculate(websocket, message['modules'])
        except websockets.ConnectionClosed:
            del connections[websocket.remote_address]


async def server(websocket, path):
    remote_address = websocket.remote_address

    if remote_address not in connections:
        connections[remote_address] = websocket

    await consumer(websocket)


start_server = websockets.serve(server, 'localhost', 5000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()