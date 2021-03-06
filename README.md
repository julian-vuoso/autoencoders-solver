# Autoencoders

## Requerimientos
Para correr el solver, es necesario tener instalado `Python 3`.

Además, debe instalarse `matplotlib` y `numpy`, lo cual se puede lograr con

- `python3 -m pip install matplotlib`
- `python3 -m pip install numpy`

Para el Variational Autoencoder es necesario tener instalado `tensorflow`, `tensorflow-datasets`, `tfds-nightly` y `scipy`, que se puede lograr con

- `python3 -m pip install tensorflow`
- `python3 -m pip install tensorflow-datasets`
- `python3 -m pip install tfds-nightly`
- `python3 -m pip install scipy`

## Ejecución

### Simple AutoEncoder
```bash
python3 simple.py
```

### Denoising AutoEncoder
```bash
python3 denoinsing.py
```

### Variational AutoEncoder
```bash
python3 vae.py
```

## Configuraciones
Todas las configuraciones de ejecución se establecen en el archivo `config.json`. A continuación, se explica a qué hace referencia cada configuración:
- **file** indica de donde se toma el conjunto de datos
- **system_threshold** indica el valor constante asignado al primer elemento de los conjuntos que se multiplicarán con w, cuyo primer elemento es w0
- **training_ratio** indica que porcentaje del training_file se usa para entrenar, quedando el restante para probar (entre 0 y 1)
- **normalize** indica el boolean de si se desea normalizar la entrada del perceptrón

- **system** indica la función de activación, cuyos valores posibles son:
    - `linear`      --> función identidad (lineal)
    - `tanh`        --> función tangente hiperbólica (no lineal)
    - `exp`         --> función sigmoide (no lineal)
- **beta** indica el multiplicador de x al utilizar una función no lineal

- **momentum** indica el boolean de si se desea aplicar la técnica de momentum o no
- **alpha** indica el valor del coeficiente alfa que se usa para momentum

- **optimizer** indica el nombre del método de optimización a utilizar para minimizar el error.
    - `None`        --> sin función de minimización
    - `Powell`      --> utilizando el método de Powell
- **opmizer_iter** cantidad de iteraciones que realiza el optimizador
- **optimizer_fev** cantidad de evaluaciones de la función de error que realiza el optimizador


- **mid_layout** es un array que indica las capas ocultas y sus dimensiones respectivas (solo para el encoder, el decoder las toma invertidas solo)
- **latent_dim** indica el valor de la dimensión de la capa latente
- **randomize_w** indica si se quiere randomizar la inicialización de los pesos
- **randomize_w_ref** indica de dónde a dónde se hace la randomización (limites)
- **randomize_w_by_len** indica el boolean si se ajusta o no el w en función del largo

- **eta** indica el valor exacto del eta a utilizar (grado de aprendizaje)
- **error_threshold** indica el delta con el cual se considerará que el error ne el entrenamiento llega a un mínimo con el que deseamos terminar de iterar
- **epochs** indica el máximo de épocas tras el cual terminar el entrenamiento
- **trust** indica el margen central de discriminación al normalizar la salida del perceptrón, de ser 
- **use_trust** indica el boolean para utilizar o no la discriminación a la salida del perceptrón 

- **denoising.pm** indica el valor de probabilidad de mutación para el denoising 


- **plot** indica el boolean de si se desea graficar

### Ejemplo 1
```json
{
	"file": "inputs/font002.txt",
	"system_threshold": 1,
	"training_ratio": 1,
	"data_random_seed": 0,
	"normalize": false,

	"system": "tanh",
	"beta": 0.9,

	"momentum": true,
	"alpha": 0.9,

	"optimizer": "Powell",
	"optimizer_iter": 10,
	"optimizer_fev": 150000,

	"mid_layout": [25],
	"latent_dim": 2,
	"randomize_w": true,
	"randomize_w_ref": 0.5,
	"randomize_w_by_len": false,

	"eta": 1e-3,
	"error_threshold": 1,
	"epochs": 1000,
	"trust": 0.5,
	"use_trust": false,

	"denoising": {
		"pm": 0.25
	},

	"plot": true
}


```

### Ejemplo 2
```json
{
	"file": "inputs/font002.txt",
	"system_threshold": 1,
	"training_ratio": 1,
	"data_random_seed": 0,
	"normalize": false,

	"system": "exp",
	"beta": 0.5,

	"momentum": true,
	"alpha": 0.9,

	"optimizer": "None",
	"optimizer_iter": 10,
	"optimizer_fev": 150000,

	"mid_layout": [25],
	"latent_dim": 2,
	"randomize_w": true,
	"randomize_w_ref": 0.5,
	"randomize_w_by_len": false,

	"eta": 1e-3,
	"error_threshold": 1,
	"epochs": 1000,
	"trust": 0.5,
	"use_trust": false,

	"denoising": {
		"pm": 0.25
	},

	"plot": false
}

```

## Presentación
Link a la presentación completa: 
https://docs.google.com/presentation/d/1qDp6P7GOqE7LNMg-ZNcKZ2pfwXffxnDBg8etEl1qv_I/edit#slide=id.p1