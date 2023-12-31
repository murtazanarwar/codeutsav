import pandas as pd


def TLR(year, toFind):
    file_path = f"overall ranking/OverallRanking_{year}.csv"
    df = pd.read_csv(file_path)
    df_sorted = df.sort_values(by="TLR", ascending=False)
    result_df = df_sorted[["Institute Name", "TLR"]]
    result_df.index = result_df.index + 1
    tlr_dict = result_df.set_index("Institute Name")["TLR"].to_dict()
    TLRlist = list(tlr_dict.values())
    i = 0
    e = len(TLRlist) - 1
    rank = 0
    while i <= e:
        mid = int(i + (e - i) / 2)
        if TLRlist[mid] == toFind:
            rank = mid + 1
            break
        elif TLRlist[mid] < toFind:
            e = mid - 1
        else:
            i = mid + 1
    rank = i + 1
    return rank


# print(TLR(2017, 79.12))


def RPC(year, toFind):
    file_path = f"overall ranking/OverallRanking_{year}.csv"
    df = pd.read_csv(file_path)
    df_sorted = df.sort_values(by="RPC", ascending=False)
    result_df = df_sorted[["Institute Name", "RPC"]]
    result_df.index = result_df.index + 1
    rpc_dict = result_df.set_index("Institute Name")["RPC"].to_dict()
    RPClist = list(rpc_dict.values())
    i = 0
    e = len(RPClist) - 1
    rank = 0
    while i <= e:
        mid = int(i + (e - i) / 2)
        if RPClist[mid] == toFind:
            rank = mid + 1
            break
        elif RPClist[mid] < toFind:
            e = mid - 1
        else:
            i = mid + 1
    rank = i + 1
    return rank


# print(RPC(2017, 79.12))


def GO(year, toFind):
    file_path = f"overall ranking/OverallRanking_{year}.csv"
    df = pd.read_csv(file_path)
    df_sorted = df.sort_values(by="GO", ascending=False)
    result_df = df_sorted[["Institute Name", "GO"]]
    result_df.index = result_df.index + 1
    GO_dict = result_df.set_index("Institute Name")["GO"].to_dict()
    GOlist = list(GO_dict.values())
    i = 0
    e = len(GOlist) - 1
    rank = 0
    while i <= e:
        mid = int(i + (e - i) / 2)
        if GOlist[mid] == toFind:
            rank = mid + 1
            break
        elif GOlist[mid] < toFind:
            e = mid - 1
        else:
            i = mid + 1
    rank = i + 1
    return rank


# print(GO(2017, 79.12))


def OI(year, toFind):
    file_path = f"overall ranking/OverallRanking_{year}.csv"
    df = pd.read_csv(file_path)
    df_sorted = df.sort_values(by="RPC", ascending=False)
    result_df = df_sorted[["Institute Name", "OI"]]
    result_df.index = result_df.index + 1
    OI_dict = result_df.set_index("Institute Name")["OI"].to_dict()
    OIlist = list(OI_dict.values())
    i = 0
    e = len(OIlist) - 1
    rank = 0
    while i <= e:
        mid = int(i + (e - i) / 2)
        if OIlist[mid] == toFind:
            rank = mid + 1
            break
        elif OIlist[mid] < toFind:
            e = mid - 1
        else:
            i = mid + 1
    rank = i + 1
    return rank


# print(OI(2017, 79.12))


def Perception(year, toFind):
    file_path = f"overall ranking/OverallRanking_{year}.csv"
    df = pd.read_csv(file_path)
    df_sorted = df.sort_values(by="RPerception", ascending=False)
    result_df = df_sorted[["Institute Name", "Perception"]]
    result_df.index = result_df.index + 1
    PRP_dict = result_df.set_index("Institute Name")["Perception"].to_dict()
    PRPlist = list(PRP_dict.values())
    i = 0
    e = len(PRPlist) - 1
    rank = 0
    while i <= e:
        mid = int(i + (e - i) / 2)
        if PRPlist[mid] == toFind:
            rank = mid + 1
            break
        elif PRPlist[mid] < toFind:
            e = mid - 1
        else:
            i = mid + 1
    rank = i + 1
    return rank


# print(Perception(2017, 79.12))
