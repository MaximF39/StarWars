class Message:
    # global = 1
    # local = 2
    # clan = 3
    # trade = 4
    # клиент чат = 5
    from_:str
    text:str
    type:int
    is_private:bool
    is_admin: bool
    date: None #Date
    