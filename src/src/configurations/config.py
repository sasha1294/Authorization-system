from fastapi import FastAPI, APIRouter

app = FastAPI(title="Base workers", debug=True)

router_set = APIRouter(prefix='/data_set', tags=['registration'])
router_update = APIRouter(prefix='/data_update', tags=['update data in db'])
router_init = APIRouter(prefix='/initialization', tags=['initialization'])
router_select = APIRouter(prefix='/data_select', tags=['select data in db'])
