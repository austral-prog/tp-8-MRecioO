def get_coordinate(tesoro):
    coordenada = tesoro[1]
    return coordenada

def convert_coordinate(coordinate):
    coordinate_N, coordinate_C = coordinate[0], coordinate[1]
    azara_cord = coordinate_N, coordinate_C
    return azara_cord

def create_record(azara_record, rui_record):
    coordinate_N, coordinate_C = azara_record[1][0], azara_record[1][1]
    azara_cord = coordinate_N, coordinate_C    
    if azara_cord == rui_record[1]:
        return azara_record + rui_record
    else:
        return 'not a match'
