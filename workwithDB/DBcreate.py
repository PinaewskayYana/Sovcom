from typing import Optional
from sqlmodel import Field,Session, SQLModel, create_engine

class Users(SQLModel, table=True):
    idNum: Optional[int] = Field(default=None, primary_key=True)
    Role: str
    login: str
    Name: str
    Pass: str
    Email: str
    phone: str


class Req(SQLModel, table=True):
    idR: Optional[int] = Field(default=None, primary_key=True)
    Category: str
    Description: str
    MinCount: Optional[int] = None


class Photo(SQLModel, table=True):
    idPh: Optional[int] = Field(default=None, primary_key=True)
    Photopath: str


class PhReq(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    idRe: Optional[int] = Field(default=None, foreign_key=Req.idR)
    idPho: Optional[int] = Field(default=None, foreign_key=Photo.idPh)


class Application(SQLModel, table=True):
    idA: Optional[int] = Field(default=None, primary_key=True)
    Cath: str
    User: Optional[int] = Field(default=None, foreign_key=Users.idNum)
    MinCount: Optional[int] = None


class ApplEl(SQLModel, table=True):
    idAe: Optional[int] = Field(default=None, primary_key=True)
    idAp: Optional[int] = Field(default=None, foreign_key=Application.idA)
    PR: Optional[int] = Field(default=None, foreign_key=PhReq.id)
    Mark: Optional[str] = None


DB_url = "postgresql+psycopg2://postgres:password@localhost:5432/SovDB" 

engine = create_engine(DB_url, echo=True)

def create_data():
    admin1 = Users(idNum= 1,Role="admin",login="kikitok",Name="Pinaevskaya Yana Aleksandrovna",Pass="12345yana",Email="zasada1926@gmail.com",phone="8912786341")
    admin2 = Users(idNum= 2,Role="admin",login="kukutok",Name="Mikhnevich Anatasia Dminrievna",Pass="12345nastya",Email="zasada1926@gmail.com",phone="8912786341")
    req1 = Req(idR =1, Category = "Транспорт",Description ="фото VIN-номера на металле",MinCount =1)
    req2 = Req(idR =2, Category = "Транспорт",Description ="фото транспортного средства снаружи с 4-х сторон + с 4-х углов ",MinCount =8)
    req3 = Req(idR =3, Category = "Транспорт",Description ="фото лобового стекла",MinCount =1)
    req4 = Req(idR =4, Category = "Транспорт",Description ="фото маркировки лобового стекла",MinCount =1)
    req5 = Req(idR =5, Category = "Транспорт",Description ="фото колеса в сборе (должны читаться размер и производитель шины)",MinCount =1)
    req6 = Req(idR =6, Category = "Транспорт",Description ="фото показаний одометра (пробег)",MinCount =1)
    req7 = Req(idR =7, Category = "Транспорт",Description ="фото салона: передняя часть салона с приборной панелью + задняя часть салона",MinCount =2)
    req8 = Req(idR =8, Category = "Транспорт",Description ="фото всех повреждений (при наличии)",MinCount =0)
    req9 = Req(idR =9, Category = "Транспорт",Description ="фото штатных ключей + ключей/брелоков/меток от дополнительных противоугонных устройств.",MinCount =1)
    req10 = Req(idR =10, Category = "Недвижимость",Description ="общий вид участка: несколько ракурсов участка для определения расстояний между объектами страхования,\
    ограждением (забором), соседними сооружениями/зданиями, подъездными дорогами, объектами повышенного риска (стройка, водоемы и т.п.)",MinCount =0)
    req11 = Req(idR =11, Category = "Недвижимость",Description ="наружные инженерные коммуникации и сооружения: электроснабжения, водоснабжения, водоотведения, \
    теплоснабжения, такие как: септик, эл.станция, трансформатор, распределительный щит, скважина, колодец, насос и т.п.",MinCount =0)
    req12 = Req(idR =12, Category = "Недвижимость",Description ="фасады строений: каждое строение с 4-х сторон, элементы внешней отделки фасадов, кровлю, фундамент;",MinCount =0)
    req13 = Req(idR =13, Category = "Недвижимость",Description ="механическую защиту окон и дверей: наружние жалюзи, решетки и т.п. крупным планом,\
    окна снаружи при отсутствии защиты;",MinCount =0)
    req14 = Req(idR =14, Category = "Недвижимость",Description ="входные (наружные) двери: с внешней стороны крупным планом;",MinCount =0)
    req15 = Req(idR =15, Category = "Недвижимость",Description ="внутреннее инженерное оборудование: сантехника, электрика (внутридомовой электрощит \
    с автоматами в открытом виде), котел, бойлер, батареи, насос, камин,  кондиционер, емкости для топлива и/или воды и т.п. - крупным планом;",MinCount =0)
    req16 = Req(idR =16, Category = "Недвижимость",Description ="пожарную сигнализацию - все элементы крупным планом;",MinCount =0)
    req17 = Req(idR =17, Category = "Недвижимость",Description ="охранная сигнализация - все элементы крупным планом;",MinCount =0)
    req18 = Req(idR =18, Category = "Недвижимость",Description ="внутреннюю отделку: общие планы каждого помещения (с двух противоположных сторон), \
    необходимо отразить все элементы внутренней отделки крупным планом: пол, потолок, стены, двери, встроенная мебель;",MinCount =0)
    req19 = Req(idR =19, Category = "Недвижимость",Description ="оконный блок: если имеются различные типы окон, то элементы конструкций \
    оконных блоков различных типов, если все окна одинаковы – то достаточно фотографий 1-го оконного блока);",MinCount =0)
    req20 = Req(idR =20, Category = "Недвижимость",Description ="дефекты и/или повреждения: имеющиеся дефекты и/или повреждения \
    отделки и основных конструкций (трещины подтеки, сколы, копоть, влага и т.п.) крупным планом;",MinCount =0)
    req21 = Req(idR =21, Category = "Недвижимость",Description ="домашнее имущество в строениях: крупным планом каждый предмет, заявляемый на страхование;",MinCount =0)
    req22 = Req(idR =22, Category = "Недвижимость",Description ="забор: \
    с каждой стороны участка забор должен быть снят с внутренней и внешней стороны (т.к. материал забора может быть разный), \
    отразить ширину и покрытие дорог, проходящих рядом с забором с каждой стороны участка,\
   отразить наличие/отсутствие искусственного рва между забором и дорогой.",MinCount =0)
    
    with Session(engine) as session:
        session.add(admin1)
        session.add(admin2)
        session.add(req1)
        session.add(req2)
        session.add(req3)
        session.add(req4)
        session.add(req5)
        session.add(req6)
        session.add(req7)
        session.add(req8)
        session.add(req9)
        session.add(req10)
        session.add(req11)
        session.add(req12)
        session.add(req13)
        session.add(req14)
        session.add(req15)
        session.add(req16)
        session.add(req17)
        session.add(req18)
        session.add(req19)
        session.add(req20)
        session.add(req21)
        session.add(req22)
      

        session.commit()

        
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_and_tables()
    create_data()

if __name__ == "__main__":
    main()
