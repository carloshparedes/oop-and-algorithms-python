from bokeh.plotting import figure, output_file, show

# Salida a un archivo HTML
output_file("graficado_simple.html")
fig = figure()
print(fig)

total_vals = int(input("Cuantos valores quieres graficar? "))   # Pide al usuario el número de valores a graficar
x_vals = list(range(total_vals))   # Crea una lista de valores x
y_vals = []   # Crea una lista vacía para los valores y

for i in x_vals:
    val = int(input(f"Valor y para {i}: "))   # Pide al usuario el valor y para cada valor x
    y_vals.append(val)  # Agrega el valor y a la lista y

fig.line(x_vals, y_vals, line_width=2)   # Grafica los valores x y y
show(fig)   # Muestra la gráfica    