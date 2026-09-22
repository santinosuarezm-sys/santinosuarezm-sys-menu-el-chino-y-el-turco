from flask import Flask, render_template

app = Flask(__name__)

MENU = {
    "Pizzas": [
        {"nombre": "Muzza", "precio": 10000, "descripcion": "Mozzarella, aceitunas y orégano."},
        {"nombre": "Fugazzeta", "precio": 10000, "descripcion": "Cebolla caramelizada y mozzarella."},
        {"nombre": "Muzza c/ jamón", "precio": 13000, "descripcion": "Mozzarella y jamón cocido."},
        {"nombre": "Napolitana", "precio": 13000, "descripcion": "Mozzarella, rodajas de tomate, ajo y albahaca."},
        {"nombre": "Jamón y morrón", "precio": 15000, "descripcion": "Jamón cocido y morrones asados."}
    ]
}

EMPANADAS = {
    "titulo": "Empanadas",
    "precios_texto": "Unidad $1.500 | Docena $25.000",
    "gustos": ["Carne", "Carne picante", "Pollo", "Jamón y queso", "Verdura"]
}

TARTAS = {
    "titulo": "Tartas",
    "precios_texto": "Porción $4.500 | Entera $15.000",
    "gustos": ["Jamón y queso", "Verdura"]
}

HAMBURGUESAS = {
    "titulo": "Hamburguesas c/guarnición",
    "lista": [
        {"nombre": "Simple", "descripcion": "Lechuga y tomate", "precio": 3000},
        {"nombre": "Completa", "descripcion": "Lechuga, tomate, jamón y queso", "precio": 4000},
        {"nombre": "Especial", "descripcion": "Lechuga, tomate, jamón, queso, huevo y cebolla caramelizada", "precio": 5000}
    ],
    "titulo_carne": "100% Carne",
    "lista_carne": [
        {"nombre": "Simple", "descripcion": "Lechuga y tomate", "precio": 4000},
        {"nombre": "Completa", "descripcion": "Lechuga, tomate, jamón y queso", "precio": 5000},
        {"nombre": "Especial", "descripcion": "Lechuga, tomate, jamón, queso, huevo y cebolla caramelizada", "precio": 6000}
    ]
}

PLATOS = {
    "titulo": "Platos",
    "lista": [
        {"nombre": "Mila sola c/ guarnición", "precio": 12000},
        {"nombre": "Mila napo c/ guarnición", "precio": 14000},
        {"nombre": "Mila a la fugazzeta c/ guarnición", "precio": 12000},
        {"nombre": "Mila al caballo c/ guarnición", "precio": 15000},
        {"nombre": "Pastel de papas", "precio": 12000},
        {"nombre": "1/4 de pollo c/ guarnición", "precio": 12000},
        {"nombre": "1/4 de pollo a la mostaza c/ guarnición", "precio": 15000},
        {"nombre": "Omelette c/ guarnición", "precio": 10000}
    ]
}

PASTAS = {
    "titulo": "Pastas",
    "lista": [
        {"nombre": "Tallarines", "precio": 10000},
        {"nombre": "Agnolottis", "precio": 12000},
        {"nombre": "Ravioles", "descripcion": "Ricota y jamón / Pollo y verdura", "precio": 12000}
    ],
    "titulo_salsas": "Salsas",
    "lista_salsas": [
        {"nombre": "Roja", "precio": 0, "texto_precio": "Sin cargo"},
        {"nombre": "Fileto", "precio": 0, "texto_precio": "Sin cargo"},
        {"nombre": "Rosa", "precio": 2500},
        {"nombre": "Crema", "precio": 2500},
        {"nombre": "Bolognesa", "precio": 4000}
    ],
    "titulo_estofados": "Estofados",
    "lista_estofados": [
        {"nombre": "Estofado de pollo", "precio": 4000},
        {"nombre": "Estofado de carne", "precio": 5000}
    ]
}

BEBIDAS = {
    "titulo": "Bebidas",
    "gaseosas": [
        {"nombre": "Línea Coca Cola", "tamanos": [{"tamano": "Lata", "precio": 2000}, {"tamano": "600 ml", "precio": 2500}, {"tamano": "1,75 L", "precio": 5000}]},
        {"nombre": "Pepsi", "tamanos": [{"tamano": "Lata", "precio": 1500}, {"tamano": "500 ml", "precio": 2000}]},
        {"nombre": "Manaos", "tamanos": [{"tamano": "600 ml", "precio": 1500}, {"tamano": "2,25 L", "precio": 3000}]},
        {"nombre": "Placer", "tamanos": [{"tamano": "500 ml", "precio": 1000}, {"tamano": "1,5 L", "precio": 2000}]},
        {"nombre": "Levite", "tamanos": [{"tamano": "1,5 L", "precio": 2500}]},
        {"nombre": "Agua", "tamanos": [{"tamano": "600 ml", "precio": 1000}, {"tamano": "2 L", "precio": 1500}]},
        {"nombre": "Soda", "tamanos": [{"tamano": "2 L", "precio": 2500}]}
    ],
    "vinos": [
        {"nombre": "Don Valentín", "precio": 5000}
    ],
    "cervezas": [
        {"nombre": "Lata Isenbeck", "precio": 2500},
        {"nombre": "Brahma", "precio": 6000},
        {"nombre": "Quilmes", "precio": 6000},
        {"nombre": "Palermo", "precio": 5000}
    ]
}

@app.route('/')
def home():
    return render_template(
        'index.html', 
        menu=MENU, 
        empanadas=EMPANADAS, 
        tartas=TARTAS, 
        hamburguesas=HAMBURGUESAS, 
        platos=PLATOS, 
        pastas=PASTAS, 
        bebidas=BEBIDAS
    )

if __name__ == '__main__':
    app.run(debug=True)