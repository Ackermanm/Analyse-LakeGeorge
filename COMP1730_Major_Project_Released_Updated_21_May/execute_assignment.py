import COMP1730_Major_Project_Released_Updated_21_May.assignment as ass

data = ass.read_dataset("assignment_lake_george_data.csv")
print(ass.largest_area(data))
print(ass.average_volume(data))
print(ass.most_average_rainfall(data))
print(ass.hottest_month(data))
ass.area_vs_volume(data)
ass.plot_volumes(ass.lake_george_simple_model(data, 55))
ass.plot_volumes(ass.lake_george_complex_model(data))
print(ass.evaluate_model(data, ass.lake_george_simple_model(data, 55)))
print(ass.evaluate_model(data, ass.lake_george_complex_model(data)))