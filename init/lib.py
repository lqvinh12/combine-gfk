def validate_cell_value(cell):
    if isinstance(cell.value, int):
        return cell.value, True
    
    if cell.value is None:
        return None, True
    
    try:
        return int(cell.value), True
    except:
        pass
    
    return None, False

def copy_cell_value(master_ws, master_row, master_col, input_ws, input_row, input_col, logger, input_file):
    input_ws_cell = input_ws.cell(input_row, input_col)
    input_ws_cell_value, is_valid = validate_cell_value(input_ws_cell)
    if is_valid:
        master_ws.cell(master_row, master_col).value = input_ws_cell_value
        
    else:
        logger.error(f'{input_file} | Wrong value of cell: {input_ws.cell(input_row, input_col).coordinate} | [{input_ws_cell.value}]')