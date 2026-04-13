# Guión de Sesiones — UT6: Microsoft Access
## AOF · Natalia Marcos Iglesias

> **Formato:** Sesiones de 60 minutos · Teoría + práctica · 10 sesiones
> **Base de datos de trabajo:** `TiendaInformatica.accdb` (se construye a lo largo del curso)

---

## Resumen del plan

| Sesión | Contenido | Tipo |
|--------|-----------|------|
| 1 | Conceptos básicos e interfaz de Access | Teoría + exploración |
| 2 | Crear tablas: Vista Diseño y tipos de datos | Teoría + práctica |
| 3 | Propiedades de campos y modificar tablas | Práctica guiada |
| 4 | Relaciones entre tablas | Teoría + práctica |
| 5 | Consultas de selección básicas | Práctica |
| 6 | Consultas avanzadas: condiciones y parámetros | Práctica + reto |
| 7 | Consultas multitabla y de resumen | Práctica |
| 8 | Consultas de referencias cruzadas y de acción | Práctica con precaución |
| 9 | Formularios: creación y uso básico | Práctica guiada |
| 10 | Formularios avanzados y proyecto integrador | Proyecto + presentación |

---

## SESIÓN 1 · Conceptos básicos e interfaz
**Duración:** 60 min

### Objetivos
- Entender qué es una base de datos y para qué sirve.
- Conocer los objetos de Access.
- Familiarizarse con la interfaz.

### Estructura

#### ⏱ 0–5 min | Activador — *"¿Para qué usamos datos?"*
Pregunta al grupo: *"¿Cuántas veces al día usáis una base de datos sin saberlo?"*
Lluvia de ideas rápida: Spotify, Netflix, el banco, el médico, la tienda online...
Escribe las respuestas en la pizarra. Conecta con el concepto de BBDD.

#### ⏱ 5–20 min | Teoría: conceptos básicos
- Definición de base de datos y SGBD.
- Modelo relacional: tablas, campos, registros.
- Clave primaria y foránea (usa el ejemplo de Clientes–Pedidos en la pizarra).
- Valor NULL vs valor 0 (con ejemplo: "no sé la edad" ≠ "tiene 0 años").
- Los 6 objetos de Access: tabla, consulta, formulario, informe, macro, módulo.

> **Truco pedagógico:** Dibuja en la pizarra una tabla de CLIENTES y una de PEDIDOS y explica la relación visualmente. Pide a alguien que identifique qué campo sería clave primaria.

#### ⏱ 20–35 min | Teoría + demo: Interfaz de Access
- Pantalla inicial: plantillas, recientes, en blanco.
- Vista Backstage (pestaña Archivo).
- Cinta de opciones: pestañas → grupos → botones. Notación: `INICIO > Portapapeles > Pegar`.
- Panel de navegación.
- Barra de estado.

> **Actividad rápida (2 min):** Con la interfaz abierta, pide que identifiquen dónde está el botón Guardar de 3 formas distintas. El primero gana un punto.

#### ⏱ 35–55 min | Práctica — Ejercicio 1.3 del cuaderno
- Crear la base de datos `TiendaInformatica.accdb` en la carpeta personal.
- Explorar la interfaz: contraer/expandir panel, cinta, cambiar vistas.
- Ejercicio 1.1 y 1.2 (vocabulario y tabla de clientes).

#### ⏱ 55–60 min | Cierre + reflexión
- Pregunta: *"¿Qué ventajas tiene Access sobre Excel para gestionar datos de una tienda?"*
- Mini-debate de 3 minutos.
- Anticipa la próxima sesión: *"La próxima sesión creamos nuestras primeras tablas."*

---

## SESIÓN 2 · Crear tablas: Vista Diseño
**Duración:** 60 min

### Objetivos
- Crear tablas en Vista Diseño.
- Conocer y elegir los tipos de datos correctos.
- Asignar clave principal.

### Estructura

#### ⏱ 0–5 min | Repaso exprés
Preguntas rápidas orales: *¿Qué es un campo? ¿Y un registro? ¿Qué es la clave primaria?*
Si alguien responde bien, hazle pasar a la pizarra a dibujar una tabla de ejemplo.

#### ⏱ 5–20 min | Teoría: tipos de datos
Presentar los tipos de dato con ejemplos cotidianos:

| Cuando pienso en... | Uso el tipo... |
|---|---|
| Nombre, dirección, teléfono | Texto corto |
| Una descripción de 3 párrafos | Texto largo |
| Precio, cantidad | Número / Moneda |
| Fecha de nacimiento | Fecha/Hora |
| ¿Está pagado? | Sí/No |
| Foto del producto | Datos adjuntos |
| Código auto-generado | Autonumeración |

> **Juego rápido (3 min):** Dictás 10 campos y los alumnos en su cuaderno apuntan el tipo de dato que usarían. Puesta en común en 2 minutos.

#### ⏱ 20–25 min | Demo: crear una tabla en Vista Diseño
Demo en proyector paso a paso:
1. Crear > Vista Diseño.
2. Definir nombre del campo, tipo, descripción.
3. Asignar clave principal.
4. Guardar.

#### ⏱ 25–55 min | Práctica guiada — Ejercicios 2.1 y práctica Clientes
- Crear la tabla `Clientes` según la ficha del cuaderno de ejercicios.
- Crear la tabla `Productos`.
- Introducir 5 registros en cada tabla en Vista Hoja de datos.

> **Circula por las mesas** durante la práctica. Presta atención a errores comunes: poner números de teléfono como tipo Número (¡no se puede poner el 0 al principio!).

#### ⏱ 55–60 min | Cierre
- ¿Por qué el teléfono es Texto corto y no Número?
- Anticipa la próxima sesión: propiedades de campo.

---

## SESIÓN 3 · Propiedades de campos y modificación de tablas
**Duración:** 60 min

### Objetivos
- Conocer y aplicar las propiedades de campo.
- Modificar tablas existentes (añadir/eliminar campos, cambiar propiedades).
- Buscar y navegar en datos.

### Estructura

#### ⏱ 0–5 min | Activador — *"El campo perfecto"*
Plantea el reto: *"Tenéis una tabla de empleados. ¿Cómo harías que sea imposible introducir un salario negativo? ¿Y que siempre aparezca 'Valencia' como ciudad por defecto?"*
Lluvia de ideas → conecta con las propiedades de campo.

#### ⏱ 5–20 min | Teoría: propiedades de campo
Explica cada propiedad con un ejemplo concreto:
- **Valor predeterminado**: ciudad "Valencia" → ahorra tiempo de entrada.
- **Regla de validación**: salario entre 1000 y 10000.
- **Texto de validación**: mensaje amigable al error.
- **Requerido**: el campo no puede quedar vacío.
- **Máscara de entrada**: guía al escribir un teléfono o DNI.
- **Título**: encabezado visible en la tabla.
- **Indexado**: mejora la velocidad de búsqueda.

#### ⏱ 20–35 min | Práctica — Ejercicio 3.1 y práctica "Modificar Clientes"
- Añadir campos Descuento y Activo con sus propiedades.
- Configurar regla de validación y texto de error.
- Probar las validaciones introduciendo datos incorrectos.

#### ⏱ 35–50 min | Práctica: buscar y reemplazar, navegación
- Usar `Ctrl+B` para buscar registros.
- Practicar la barra de navegación de registros.
- Reemplazar datos con la herramienta Buscar y Reemplazar.

#### ⏱ 50–58 min | Actividad: "Cazarrores"
Prepara de antemano una tabla con 5 errores de diseño (campo precio como Texto, sin clave primaria, teléfono como Número, etc.). Por parejas tienen que encontrar todos los errores y proponer la corrección. El equipo que encuentre más errores gana.

#### ⏱ 58–60 min | Cierre
Resumen de propiedades. Anuncia la próxima sesión: relaciones.

---

## SESIÓN 4 · Relaciones entre tablas
**Duración:** 60 min

### Objetivos
- Entender los tipos de relaciones (1:1, 1:N, N:M).
- Crear relaciones con integridad referencial.
- Comprender las actualizaciones y eliminaciones en cascada.

### Estructura

#### ⏱ 0–8 min | Activador visual — "El mundo de las relaciones"
Dibuja en la pizarra tres escenarios y pide que clasifiquen el tipo de relación:
- Alumno ↔ Carnet de biblioteca → 1:1
- Madre ↔ Hijos → 1:N
- Estudiante ↔ Asignaturas → N:M

Luego conecta con el mundo de la tienda: Cliente ↔ Pedidos.

#### ⏱ 8–22 min | Teoría: tipos de relaciones y creación
- Repaso visual de los 3 tipos con ejemplos del contexto de la tienda.
- Cómo crear relaciones en Access (demo en proyector):
  - Herramientas de base de datos > Relaciones.
  - Mostrar tabla, arrastrar campo.
  - Integridad referencial: qué significa y por qué es importante.
  - Cascada: actualizar y eliminar.

> **Pregunta provocadora:** *"¿Qué pasaría si borramos el cliente C001 y tiene 20 pedidos? ¿Y si tenemos integridad referencial?"*

#### ⏱ 22–45 min | Práctica — Crear relaciones de TiendaInformatica
- Crear tabla DetallesPedido.
- Crear las 3 relaciones con integridad referencial y actualización en cascada.
- Probar la integridad: intentar insertar un pedido con un cliente inexistente → debe dar error.

#### ⏱ 45–55 min | Ejercicio 4.2 en parejas
Responder las preguntas teóricas sobre integridad referencial. Puesta en común en 5 minutos.

#### ⏱ 55–60 min | Cierre
Dibuja el diagrama ER de la base de datos en la pizarra con la ayuda del grupo.

---

## SESIÓN 5 · Consultas de selección básicas
**Duración:** 60 min

### Objetivos
- Crear consultas de selección en Vista Diseño.
- Usar criterios simples, ordenar resultados.
- Crear campos calculados.

### Estructura

#### ⏱ 0–5 min | Activador — "¿Qué quiero saber?"
*"Si sois el jefe de la tienda, ¿qué tres preguntas haríais a vuestra base de datos ahora mismo?"*
Escribid las preguntas → son exactamente para lo que sirven las consultas.

#### ⏱ 5–20 min | Teoría: consultas de selección y cuadrícula QBE
- Tipos de consultas (selección, acción, SQL).
- Vista Diseño: cuadrícula QBE, zona de tablas.
- Filas: Campo, Tabla, Orden, Mostrar, Criterios, O.
- Demo en proyector: consulta simple sobre Clientes de Valencia.

#### ⏱ 20–50 min | Práctica — Ejercicios sesión 5
- Consultas ConsClientesValencia, ConsProductosCara, ConsPedidosPendientes.
- Campo calculado: ConsPrecioIVA.
- Consultas con comodines: ConsNombresA, ConsEmailGoogle.

> **Reto extra** para los rápidos: ConsClientesCumpleanos usando `Month(Date())`.

#### ⏱ 50–58 min | Mini-exposición
Un alumno voluntario muestra su consulta ConsClientesCumpleanos al resto de la clase y explica cómo funciona la expresión.

#### ⏱ 58–60 min | Cierre
¿Para qué sirve el asterisco (*) en la cuadrícula QBE? ¿Cuándo activaríamos/desactivaríamos la casilla Mostrar?

---

## SESIÓN 6 · Consultas avanzadas: condiciones y parámetros
**Duración:** 60 min

### Objetivos
- Usar operadores avanzados: Entre, In, Es Nulo, Como.
- Combinar condiciones con Y y O.
- Crear consultas con parámetros.

### Estructura

#### ⏱ 0–5 min | Repaso activo
"Kahoot" rápido (5 preguntas de repaso sobre consultas básicas). Usa kahoot.it o quizlet.com para hacerlo más dinámico.

#### ⏱ 5–20 min | Teoría: operadores avanzados y parámetros
- Operadores: `Entre`, `In`, `Es Nulo`, `Como` (con comodines * ? # []).
- Condiciones múltiples: Y (misma fila) vs. O (filas distintas).
- Parámetros: por qué son útiles, sintaxis entre corchetes.

> **Ejemplo en pizarra:** consulta que muestra alumnos de Valencia Y nacidos entre 1980–1990, O de Madrid de cualquier fecha. Dibuja la cuadrícula QBE.

#### ⏱ 20–50 min | Práctica — Ejercicios sesión 6
- Consultas con parámetros: ConsBuscarCiudad, ConsBuscarPrecio, ConsBuscarFechas.
- Consulta ConsClientesSinPedidos (composición externa + Es Nulo).
- Ejercicio 6.1 teórico en parejas.

#### ⏱ 50–58 min | Dinámica: "El detective"
Por tríos, cada grupo recibe una pregunta de negocio (*"¿Qué clientes de Madrid tienen más de 30 años y no han comprado en 2024?"*) y deben diseñar la consulta. Comparten el resultado.

#### ⏱ 58–60 min | Cierre
¿Cuándo usarías un parámetro en lugar de poner el valor directamente en el criterio?

---

## SESIÓN 7 · Consultas multitabla y de resumen
**Duración:** 60 min

### Objetivos
- Crear consultas que combinan varias tablas.
- Entender y usar funciones de agregado.
- Agrupar registros.

### Estructura

#### ⏱ 0–5 min | Activador — "El informe del jefe"
*"El jefe quiere saber el total de ventas por ciudad. Los datos están en 3 tablas distintas. ¿Cómo lo hacemos?"*
Desglosa el problema paso a paso con el grupo.

#### ⏱ 5–20 min | Teoría: consultas multitabla y resumen
- Consulta multitabla: añadir varias tablas, línea de combinación.
- Composición interna vs. externa (repaso rápido).
- Consultas de resumen: botón Totales, fila Total:.
- Funciones: Suma, Promedio, Cuenta, Mín, Max, AgruparPor, Dónde.

> **Demostración:** crear ConsResumenCiudad en proyector, paso a paso.

#### ⏱ 20–50 min | Práctica — Ejercicios sesión 7
- ConsClientesPedidos (multitabla, 2 tablas).
- ConsDetallesCompletos (3 tablas + campo calculado subtotal).
- ConsResumenCiudad, ConsEstadisticaProductos.
- ConsVentasTotales.

#### ⏱ 50–58 min | Reflexión en parejas
Ejercicio 7 de reflexión: ¿qué decisiones de negocio puedes tomar con estas consultas? Cada pareja comparte una idea.

#### ⏱ 58–60 min | Cierre
¿Por qué NULL no se cuenta en las funciones de agregado? Pon un ejemplo de cuándo esto importa.

---

## SESIÓN 8 · Referencias cruzadas y consultas de acción
**Duración:** 60 min

### Objetivos
- Crear consultas de referencias cruzadas con el asistente.
- Entender y ejecutar consultas de acción con precaución.

### Estructura

#### ⏱ 0–5 min | Activador — "La tabla pivote"
Muestra una tabla de ventas por mes y empleado en Excel. *"Access puede hacer esto automáticamente. Se llama consulta de referencias cruzadas."* Genera expectativa.

#### ⏱ 5–15 min | Teoría: consultas de referencias cruzadas
- Concepto: tabla de doble entrada (filas vs. columnas de agrupación).
- Asistente paso a paso: origen → filas → columnas → valor → nombre.
- Demo en proyector: CruzVentasMensuales.

#### ⏱ 15–25 min | Práctica: CruzVentasMensuales
Cada alumno crea la consulta de referencias cruzadas guiándose por los ejercicios.

#### ⏱ 25–35 min | Teoría: consultas de acción (con PRECAUCIÓN)
- Tipos: Actualización, Creación de tabla, Datos anexados, Eliminación.
- Flujo seguro: diseñar como selección → revisar en Vista Hoja de datos → convertir → ejecutar.
- Mensaje de confirmación de Access.

> **Advertencia dramática:** *"Estas consultas son como el botón rojo nuclear: revisa siempre antes de ejecutar. No hay Ctrl+Z para deshacer 1000 registros borrados."*

#### ⏱ 35–55 min | Práctica — Ejercicios sesión 8 (de menor a mayor riesgo)
- SubirPrecio10 (actualización).
- CrearClientesVIP (creación de tabla — la más segura).
- AnexarClientesPrueba (datos anexados).
- EliminarPedidosAntiguos (¡solo si han completado el resto!).

#### ⏱ 55–60 min | Cierre + reflexión
Ejercicio 8.1 oral: pregunta rápida a varios alumnos sobre las diferencias entre tipos de consulta de acción.

---

## SESIÓN 9 · Formularios: creación y uso básico
**Duración:** 60 min

### Objetivos
- Crear formularios con el asistente y autoformulario.
- Editar datos a través de un formulario.
- Explorar la Vista Diseño básica.

### Estructura

#### ⏱ 0–5 min | Activador visual
Muestra dos formas de introducir datos: la Vista Hoja de datos vs. un formulario bien diseñado con colores, logo y campos bien organizados. *"¿Cuál preferiríais usar cada día en vuestro trabajo?"* El formulario gana casi siempre. Eso es lo que vamos a crear hoy.

#### ⏱ 5–15 min | Teoría: tipos de formularios y asistente
- Para qué sirven los formularios (entrada de datos, visualización amigable).
- Opciones de creación: Formulario automático, en blanco, asistente, diseño.
- Distribuciones: En columnas, Tabular, Hoja de datos, Justificado.
- Vista Formulario vs Vista Diseño vs Vista Presentación.

#### ⏱ 15–25 min | Demo: crear FrmClientes con el asistente
Demo en proyector. Mostrar todas las opciones del asistente paso a paso. Resultado final en Vista Formulario.

#### ⏱ 25–50 min | Práctica — Ejercicios sesión 9
- Crear FrmClientes (columnas) y FrmProductos (tabular).
- Introducir datos a través de los formularios.
- Navegar entre registros con la barra de navegación.
- Explorar las tres secciones de la Vista Diseño: encabezado, detalle, pie.

#### ⏱ 50–58 min | Reto por equipos
Por parejas: personalizar visualmente FrmClientes en 8 minutos. Gana la pareja con el formulario más bonito y funcional (votación anónima de la clase).

#### ⏱ 58–60 min | Cierre
¿Qué propiedad del formulario cambiarías para que al abrirlo vaya directamente a introducir un registro nuevo sin mostrar los existentes?

---

## SESIÓN 10 · Formularios avanzados y proyecto final
**Duración:** 60 min

### Objetivos
- Crear subformularios.
- Configurar propiedades avanzadas.
- Presentar y defender el proyecto integrador.

### Estructura

#### ⏱ 0–10 min | Teoría: subformularios y propiedades avanzadas
- Para qué sirve un subformulario (relaciones 1:N).
- Cómo crearlo: usando el asistente de subformularios o arrastrar desde el panel.
- Propiedades importantes: Origen del registro, Vista predeterminada, Permitir agregar/eliminar, Entrada de datos, Modal.
- Pestaña Formato: título, botones de navegación, selectores de registro.

#### ⏱ 10–30 min | Práctica: FrmPedidosCompleto con subformulario
- Crear el formulario principal (Pedidos) y añadir el subformulario (DetallesPedido).
- Verificar que la vinculación funciona correctamente.
- Añadir campo calculado de total en el pie del subformulario.

#### ⏱ 30–45 min | Trabajo en proyecto integrador
Tiempo libre para trabajar en las partes 1, 2 y 3 del proyecto final. El profesor/a circula y da apoyo individualizado.

> **Sugerencia:** anima a los más avanzados a crear el formulario de menú principal con botones.

#### ⏱ 45–60 min | Presentaciones finales (5 min/grupo o individual)
Cada alumno/pareja muestra brevemente:
- Su base de datos funcionando.
- La consulta que más le ha costado y cómo la resolvió.
- Algo que mejoraría o ampliaría.

> **Evaluación entre iguales:** durante cada presentación, el resto anota en una tarjeta algo que les ha gustado o una pregunta que quieran hacer.

---

## Notas generales para el docente

### Recursos recomendados
- [AulaClick Access 2019](https://www.aulaclic.es/access-2019/) — referencia libre y en español.
- Kahoot para repasos: preparar preguntas de 30 segundos para las actividades de inicio.
- Uso del proyector para demos en tiempo real (fundamental en las sesiones 2, 4, 5 y 7).

### Gestión del ritmo
- Los alumnos más rápidos siempre tienen un "reto extra" disponible.
- Si el grupo va lento, las consultas de referencias cruzadas (final sesión 8) pueden moverse a la siguiente sesión.
- Los subformularios son opcionales si el tiempo aprieta; el proyecto puede simplificarse.

### Evaluación continua
- Observación durante las prácticas.
- Entrega de la base de datos `TiendaInformatica.accdb` al final del bloque.
- Las consultas deben ejecutarse correctamente y mostrar los resultados esperados.
- El formulario final debe ser funcional y bien diseñado.

### Errores comunes a vigilar
- Teléfonos como tipo Número (pierden el cero inicial).
- No asignar clave primaria antes de guardar.
- Ejecutar consultas de acción sin revisar antes en Vista Hoja de datos.
- Confundir "Actualizar en cascada" con "Eliminar en cascada".
- Olvidar los corchetes en los parámetros de consulta.
