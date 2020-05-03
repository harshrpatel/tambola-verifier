import pandas as pd


def get_data_from_excel(file_path="asset/movie_ticket.xlsx"):
    response_dict = {}
    df = pd.read_excel(file_path, sheet_name="Sheet1")

    list_of_values = df.values.flatten()
    s_list = [i.strip() for i in list_of_values]
    response_dict["ticket"] = s_list
    response_dict["shape"] = df.shape

    df_pattern = pd.read_excel(file_path, sheet_name="Sheet2")
    p_dict = df_pattern.to_dict()
    t_dict = {}

    for k_p, v_p in p_dict.items():
        l = set()
        for k_d, v_d in v_p.items():
            if isinstance(v_d, str):
                l.add(v_d.strip())
        t_dict[k_p] = l

    response_dict["patterns"] = t_dict

    with open("asset/movies_ticket.txt", 'w') as f:
        f.write(str(response_dict["ticket"]) + "\n")
        f.write(str(response_dict["patterns"]))
    return response_dict
