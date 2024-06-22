import pandas as pd
import numpy as np
import datetime
from scipy.special import factorial

def create_ordenes_financieras(df, month_to_predict, ordenes_aprobadas=None, REGION=None, year_month=None): # year_month must be "2024-08"
    """
    Create financial orders based on predicted values and average daily weights.

    Args:
    - df (pd.DataFrame): Dataframe containing order data.
    - month_to_predict (pd.Series): Series containing orders for the month to predict.
    - ordenes_aprobadas (int, optional): Approved orders.
    - REGION (str, optional): Region for which to create orders.
    - year_month (str, optional): Year and month in 'YYYY-MM' format.

    Returns:
    - pd.DataFrame: DataFrame with financial/forecasted orders.
    """
    print(f"Function called with REGION: {REGION}")
    ordenes_financieras = pd.DataFrame()

    if REGION == "SS":
        try:
            print("Processing for REGION SS")
            orders = df.copy()
            orders = orders[orders["COUNTRY"] != "BR"]
            start_date = datetime.datetime.strptime("2024-01-01", "%Y-%m-%d").date()
            orders = orders[orders["FECHA"] >= start_date]

            orders['FECHA'] = pd.to_datetime(orders['FECHA'])
            pivot_table = orders.pivot_table(index='FECHA', columns='COUNTRY', values='ORDERS', aggfunc='mean', fill_value=0)
            SS = pivot_table.sum(axis=1)
            SS.name = 'SS'
            pivot_table_with_total = pd.merge(pivot_table, SS.to_frame(), on="FECHA", how="inner")
            pivot_table_percentage = pivot_table_with_total.div(pivot_table_with_total['SS'], axis=0) * 100
            pivot_table_percentage = pivot_table_percentage.round(2)
            average_weight_by_day = pivot_table_percentage.groupby(pivot_table_percentage.index.day).mean()
            if month_to_predict.shape[0]==30:
                average_weight_by_day = average_weight_by_day[:-1] # quitar el 31 de month
            else:
                print("The month_to_predict is not 30.")
            # average_weight_by_day = average_weight_by_day[:-1] # quitar el 31 de month
            date_strings = [f'{year_month}-{day}' for day in average_weight_by_day.index]
            # date_strings = [f'2024-09-{day}' for day in average_weight_by_day.index]

            average_weight_by_day.index = pd.to_datetime(date_strings, format='%Y-%m-%d')
            average_weight_by_day.index = average_weight_by_day.index.strftime('%Y-%m-%d')
            # series_reindexed = month_to_predict

            series_reindexed = month_to_predict.reindex(average_weight_by_day.index, fill_value=0)
            # if there are diferent numbers of approved orders then use it.
            if ordenes_aprobadas:
                ordenes_aprobadas = ordenes_aprobadas
                prop_ordenes_dias_mes = series_reindexed/series_reindexed.sum()
                series_reindexed = prop_ordenes_dias_mes*ordenes_aprobadas
            # series_reindexed_modif.head()
            series_reindexed.index = pd.to_datetime(series_reindexed.index, format='%Y-%m-%d')
            series_reindexed.index = series_reindexed.index.strftime('%Y-%m-%d')
            # if series_reindexed.shape[0]==31:
            #     average_weight_by_day.set_index(pd.date_range("2024-08-01","2024-08-31"), inplace=True)
            # else:
            #     average_weight_by_day.set_index(pd.date_range("2024-08-01","2024-08-30"), inplace=True)
            # ordenes_financieras = average_weight_by_day.mul(series_reindexed, axis=0) / 100
            ordenes_financieras = average_weight_by_day.mul(series_reindexed, axis=0) / 100
            orden_dias = ['CO', 'MX', 'EC', 'PE', 'CL', 'AR', 'UY', 'CR', 'SS']
            ordenes_financieras = ordenes_financieras.filter(orden_dias)
            ordenes_financieras = ordenes_financieras.reset_index()
            ordenes_financieras.rename(columns={"index": "FECHA"}, inplace=True)
        except Exception as e:
            print(f"An error occurred while processing REGION 'SS': {e}")
        
    elif REGION == "BR":
        try:
            print("Processing for REGION BR")
            orders=df.copy()
            orders = orders[orders["COUNTRY"] == "BR"]
            start_date = datetime.datetime.strptime("2024-01-01", "%Y-%m-%d").date()
            orders = orders[orders["FECHA"] >= start_date]
            # -------------------------------------------------
            orders['FECHA'] = pd.to_datetime(orders['FECHA'])
            pivot_table = orders.pivot_table(index='FECHA', columns='COUNTRY', values='ORDERS', aggfunc='mean', fill_value=0)
            brasil = pivot_table.sum(axis=1)
            brasil.name = 'brasil'
            pivot_table_with_total = pd.merge(pivot_table, brasil.to_frame(), on="FECHA", how="inner")
            pivot_table_percentage = pivot_table_with_total.div(pivot_table['BR'], axis=0) * 100
            pivot_table_percentage = pivot_table_percentage.round(2)
            average_weight_by_day = pivot_table_percentage.groupby(pivot_table_percentage.index.day).mean()
            if month_to_predict.shape[0]==30:
                average_weight_by_day = average_weight_by_day[:-1] # quitar el 31 de month
            else:
                print("The month_to_predict is not 30.")

            date_strings = [f'{year_month}-{day}' for day in average_weight_by_day.index]
            average_weight_by_day.index = pd.to_datetime(date_strings, format='%Y-%m-%d')
            average_weight_by_day.index = average_weight_by_day.index.strftime('%Y-%m-%d')
            # series_reindexed = month_to_predict

            series_reindexed = month_to_predict.reindex(average_weight_by_day.index, fill_value=0)
            # if there are diferent numbers of approved orders then use it.
            if ordenes_aprobadas:
                ordenes_aprobadas = ordenes_aprobadas
                prop_ordenes_dias_mes = series_reindexed/series_reindexed.sum()
                series_reindexed = prop_ordenes_dias_mes*ordenes_aprobadas
            # series_reindexed_modif.head()
            series_reindexed.index = pd.to_datetime(series_reindexed.index, format='%Y-%m-%d')
            series_reindexed.index = series_reindexed.index.strftime('%Y-%m-%d')
            ordenes_financieras = average_weight_by_day.mul(series_reindexed, axis=0) / 100
            ordenes_financieras=ordenes_financieras.filter(["BR"])
            ordenes_financieras = ordenes_financieras.reset_index()
            ordenes_financieras.rename(columns={"index": "FECHA"}, inplace=True)
        except Exception as e:
            print(f"An error occurred while processing REGION 'BR': {e}")
    else:
        print(f"Unknown REGION: {REGION}")
        
    return ordenes_financieras

def create_curva_ordenes(df,REGION):
    """
    Create order curve based on order distribution throughout the week.

    Args:
    - df (pd.DataFrame): Dataframe containing order information.

    Returns:
    - pd.DataFrame: DataFrame with order curve.
    """
    if REGION=="SS":
        orders = df.copy()
        orders = orders[orders["COUNTRY"] != "BR"]
        start_date = datetime.datetime.strptime("2024-01-01", "%Y-%m-%d").date()
        orders = orders[orders["FECHA"] >= start_date]

        orders['FECHA'] = pd.to_datetime(orders['FECHA'])
        orders['INTERVALO'] = pd.to_datetime(orders['INTERVALO'], format='%H:%M:%S').dt.time
        orders['DAY_OF_WEEK'] = orders['FECHA'].dt.day_name()

        pivot_table = orders.pivot_table(index='INTERVALO', columns='DAY_OF_WEEK', values='ORDERS', aggfunc='mean', fill_value=0)
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        pivot_table.columns = pd.CategoricalIndex(pivot_table.columns, categories=weekdays, ordered=True)
        pivot_table = pivot_table.sort_index(axis=1)

        total_general = pivot_table.sum(axis=0)
        total_general.name = 'Total general'

        pivot_table_with_total = pd.concat([pivot_table, total_general.to_frame().T])

        pivot_table_percentage = pivot_table_with_total.div(pivot_table_with_total.loc['Total general']) * 100
        pivot_table_percentage = pivot_table_percentage.round(2)
        curva_ordenes = pivot_table_percentage.drop(pivot_table_percentage.tail(1).index)  # drop last row
        curva_ordenes = curva_ordenes.reset_index()
        curva_ordenes.rename(columns={"index": "intervalo"}, inplace=True)
        curva_ordenes.set_index("intervalo", inplace=True)
        curva_ordenes = curva_ordenes / 100

    elif REGION == "BR":
        orders=df.copy()
        orders = orders[orders["COUNTRY"] == "BR"]
        start_date = datetime.datetime.strptime("2024-01-01", "%Y-%m-%d").date()
        orders = orders[orders["FECHA"] >= start_date]
        # -------------------------------------------------
        orders['FECHA'] = pd.to_datetime(orders['FECHA'])
        orders['INTERVALO'] = pd.to_datetime(orders['INTERVALO'], format='%H:%M:%S').dt.time
        orders['DAY_OF_WEEK'] = orders['FECHA'].dt.day_name()
        #avg_orders = orders.groupby(['DAY_OF_WEEK', 'HOUR', 'COUNTRY'])['ORDERS'].mean().reset_index()

        pivot_table = orders.pivot_table(index='INTERVALO', columns='DAY_OF_WEEK', values='ORDERS', aggfunc='mean', fill_value=0)
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        pivot_table.columns = pd.CategoricalIndex(pivot_table.columns, categories=weekdays, ordered=True)
        pivot_table = pivot_table.sort_index(axis=1)

        total_general = pivot_table.sum(axis=0)
        total_general.name = 'Total general'

        pivot_table_with_total = pd.concat([pivot_table, total_general.to_frame().T])

        pivot_table_percentage = pivot_table_with_total.div(pivot_table_with_total.loc['Total general']) * 100
        pivot_table_percentage = pivot_table_percentage.round(2)
        #curva_ordenes = pivot_table_percentage[:-1]
        curva_ordenes=pivot_table_percentage.drop(pivot_table_percentage.tail(1).index) # drop last row
        curva_ordenes=curva_ordenes.reset_index()
        curva_ordenes.rename(columns={"index":"intervalo"},inplace=True)
        curva_ordenes.set_index("intervalo", inplace=True)
        curva_ordenes=curva_ordenes/100
        
    return curva_ordenes


def distribute_orders(ordenes_financieras, curva_ordenes):
    """
    Distribute financial orders according to the order curve.

    Args:
    - ordenes_financieras (pd.DataFrame): Dataframe containing financial orders.
    - curva_ordenes (pd.DataFrame): Dataframe containing order curve.

    Returns:
    - pd.DataFrame: DataFrame with distributed orders by day and interval.
    """

    # Create a MultiIndex for the new DataFrame
    index = pd.MultiIndex.from_product([ordenes_financieras['FECHA'].unique(), curva_ordenes.index], names=['FECHA', 'Intervalo'])
    df3 = pd.DataFrame(index=index, columns=ordenes_financieras.columns[1:], data=np.zeros((len(index), len(ordenes_financieras.columns[1:]))))
    df3 = df3.reset_index()

    def get_day_of_week(date):
        return pd.to_datetime(date).strftime('%A')

    for i, row in ordenes_financieras.iterrows():
        day_of_week = get_day_of_week(row['FECHA'])
        values = row[1:].values
        for j, interval in enumerate(curva_ordenes.index):
            proportion = curva_ordenes.loc[interval, day_of_week]
            # Ensure the result is a flat array for assignment
            distributed_values = values * proportion
            df3.loc[(df3['FECHA'] == row['FECHA']) & (df3['Intervalo'] == interval), ordenes_financieras.columns[1:]] = distributed_values
    
    return df3



def distribute_inflow_intraday(inflow, df3, SERVICE_USER_TYPE, SERVICE, REGION):
    """
    Distribute inflow according to the orders curve.

    Args:
    - inflow (pd.DataFrame): Dataframe containing inflow.
    - df3 (pd.DataFrame): Dataframe containing order curve.

    Returns:
    - pd.DataFrame: DataFrame with distributed orders by day and interval.
    """
    inflow=inflow.sort_values(by=["FECHA", "INTERVALO"], ascending=True)
    inflow['mes'] = pd.to_datetime(inflow['FECHA']).dt.strftime("%B")
    inflow['semana'] = pd.to_numeric(pd.to_datetime(inflow['FECHA']).dt.strftime('%U'))
    inflow['dia'] = pd.to_datetime(inflow['FECHA']).dt.strftime('%A')
    meses = ['March','April','May']
    inflow = inflow[(inflow['mes'].isin(meses))]
    inflow.reset_index(drop=True, inplace=True)

    tabla_orders = pd.pivot_table(inflow,values='ORDERS',index=['REGION','INTERVALO'],columns='FECHA',aggfunc='sum')
    df_user_type= inflow[inflow['SERVICE_USER_TYPE']==SERVICE_USER_TYPE]
    df_user_type= inflow[inflow['SERVICE']==SERVICE] 
    df_user_type.reset_index(drop=True, inplace=True)
    inflow_df_user_type = pd.pivot_table(df_user_type, values='INFLOW', index=['REGION', 'INTERVALO'], columns='FECHA', aggfunc='sum')

    CR = inflow_df_user_type.div(tabla_orders)
    CR= CR.reset_index()
    CR = pd.DataFrame(CR)

    CR = CR.melt(id_vars = ['REGION','INTERVALO'],var_name='FECHA',value_name='CR')
    CR=CR[CR["REGION"]==REGION]

    CR_dimen= CR.filter(['FECHA','INTERVALO', 'CR'])
    CR_dimen['DAY_OF_WEEK'] = pd.to_datetime(CR_dimen['FECHA']).dt.day_name()
    CR_pivot_table = CR_dimen.pivot_table(index='INTERVALO', columns='DAY_OF_WEEK', values='CR', aggfunc='mean')
    CR_pivot_table = CR_pivot_table[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]

    ordenes_dimen=df3.filter(["FECHA","Intervalo",REGION])
    ordenes_dimen["DAY_OF_WEEK"] = pd.to_datetime(ordenes_dimen["FECHA"]).dt.day_name()

    curva_cr = CR_pivot_table.reset_index()
    curva_cr = pd.DataFrame(curva_cr)

    # """para cada fila en órdenes_dimen, este código multiplica el valor SS por el factor de ajuste correspondiente del marco de datos curva_cr basado en las columnas Intervalo y DAY_OF_WEEK, y almacena el resultado en una nueva columna llamada Adjusted_SS."""
    ordenes_dimen[f'Adjusted_+{REGION}'] = ordenes_dimen.apply(
        lambda row: row[REGION] * curva_cr[curva_cr['INTERVALO'] == row['Intervalo']][row['DAY_OF_WEEK']].values[0], axis=1
    )

    result = ordenes_dimen.pivot(index='FECHA', columns='Intervalo', values=f'Adjusted_+{REGION}').reset_index()
    result.columns.name = None
    result['Día'] = pd.to_datetime(result['FECHA']).dt.day_name(locale='es_ES')
    result['Forecast Inflow'] = result.drop(columns=['FECHA', 'Día']).sum(axis=1)
    result = result[['FECHA', 'Día', 'Forecast Inflow'] + list(result.columns[1:-2])]

    return result


def distribute_aht_intraday(inflow, df3, SERVICE_USER_TYPE, SERVICE, REGION, result, aht_meta):
    """
    Distribute inflow according to the orders curve.

    Args:
    - inflow (pd.DataFrame): Dataframe containing inflow.
    - df3 (pd.DataFrame): Dataframe containing order curve.

    Returns:
    - pd.DataFrame: DataFrame with distributed orders by day and interval.
    """
    inflow=inflow.sort_values(by=["FECHA", "INTERVALO"], ascending=True)
    inflow['mes'] = pd.to_datetime(inflow['FECHA']).dt.strftime("%B")
    inflow['semana'] = pd.to_numeric(pd.to_datetime(inflow['FECHA']).dt.strftime('%U'))
    inflow['dia'] = pd.to_datetime(inflow['FECHA']).dt.strftime('%A')
    meses = ['March','April','May']
    inflow = inflow[(inflow['mes'].isin(meses))]
    inflow.reset_index(drop=True, inplace=True)

    tabla_orders = pd.pivot_table(inflow,values='ORDERS',index=['REGION','INTERVALO'],columns='FECHA',aggfunc='sum')
    df_user_type= inflow[inflow['SERVICE_USER_TYPE']==SERVICE_USER_TYPE]
    df_user_type= inflow[inflow['SERVICE']==SERVICE] 
    df_user_type.reset_index(drop=True, inplace=True)
    # inflow_df_user_type = pd.pivot_table(df_user_type, values='INFLOW', index=['REGION', 'INTERVALO'], columns='FECHA', aggfunc='sum')

    df_user_type["aht_inflow"]=df_user_type["SUM_AHT"].astype(float)/df_user_type["INFLOW"]/60
    aht_users = pd.pivot_table(df_user_type, values='aht_inflow', index=['REGION', 'INTERVALO'], columns='FECHA', aggfunc='mean')
    aht_users= aht_users.reset_index()
    aht_users = pd.DataFrame(aht_users)
    aht_users = aht_users.melt(id_vars = ['REGION','INTERVALO'],var_name='FECHA',value_name='aht')
    aht_users = aht_users[aht_users["REGION"]==REGION] 
    aht_users.reset_index(drop=True, inplace=True)
    aht_users["aht"]=aht_users["aht"].astype(float)
    aht_users["aht"]=aht_users["aht"]
    aht_dimen= aht_users.filter(['FECHA','INTERVALO', 'aht'])
    aht_dimen["DAY_OF_WEEK"] = pd.to_datetime(aht_dimen["FECHA"]).dt.day_name()
    aht_dimen= aht_users.filter(['FECHA','INTERVALO', 'aht'])
    aht_dimen["DAY_OF_WEEK"] = pd.to_datetime(aht_dimen["FECHA"]).dt.day_name()
    aht_mean = aht_dimen.groupby(['INTERVALO', 'DAY_OF_WEEK'])['aht'].mean().unstack()
    aht_mean = aht_mean[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]
    # total 1
    total_general = aht_mean.mean(axis=0)
    total_general.name = 'Promedio_dia'
    aht_mean = pd.concat([aht_mean, total_general.to_frame().T])
    # total 2
    total_general = aht_mean.loc['Promedio_dia']/aht_mean.loc['Promedio_dia'].mean(axis=0)
    total_general.name = 'Promedio_semana'
    aht_mean = pd.concat([aht_mean, total_general.to_frame().T])

    aht_percent = (aht_mean.iloc[:-1]/aht_mean.loc["Promedio_dia"])
    aht_percent = pd.concat([aht_percent, aht_mean.iloc[-1:]])
    aht_percent = aht_percent*100
    def adjust_values(x):
        if x > 105:
            return 105
        elif x < 95:
            return 95
        else:
            return x

    # Apply the function to the entire DataFrame
    aht_percent.iloc[:-1] = aht_percent.iloc[:-1].applymap(adjust_values)  # tarea para mañana agregar esta logica arriba

    aht_percent=aht_percent.drop("Promedio_dia", axis=0)
    aht_meta = aht_meta
    # aht_meta_dia = aht_meta*aht_percent.loc["Promedio_semana"]/100
    aht_percent = aht_percent*(aht_meta*aht_percent.loc["Promedio_semana"]/100)/100
    curva_aht = aht_percent.reset_index()
    curva_aht.rename(columns={'index':'INTERVALO'}, inplace=True)
    # curva_cr.set_index("INTERVALO", inplace=True)
    # curva_cr.columns.name = None
    curva_aht = pd.DataFrame(curva_aht.iloc[:-1])
    # """para cada fila en órdenes_dimen, este código multiplica el valor SS por el factor de ajuste correspondiente del marco de datos curva_cr basado en las columnas Intervalo y DAY_OF_WEEK, y almacena el resultado en una nueva columna llamada Adjusted_SS."""
    ordenes_dimen=df3.filter(["FECHA","Intervalo",REGION])
    ordenes_dimen["DAY_OF_WEEK"] = pd.to_datetime(ordenes_dimen["FECHA"]).dt.day_name()

    ordenes_dimen['aht'] = ordenes_dimen.apply(
        lambda row: curva_aht[curva_aht['INTERVALO'] == row['Intervalo']][row['DAY_OF_WEEK']].values[0], axis=1
    )
    result2 = ordenes_dimen.pivot(index='FECHA', columns='Intervalo', values='aht').reset_index()
    result2.columns.name = None
    result2['Día'] = pd.to_datetime(result2['FECHA']).dt.day_name(locale='es_ES')
    result2['Forecast AHT'] = result2.drop(columns=['FECHA', 'Día']).sum(axis=1)
    result2 = result2[['FECHA', 'Día', 'Forecast AHT'] + list(result2.columns[1:-2])]
    df1 = result.drop(columns=['FECHA', 'Día', 'Forecast Inflow'])
    df2 = result2.drop(columns=['FECHA', 'Día', 'Forecast AHT'])

    new_forecast_aht = []

    for i in range(len(df1)):
        sumproduct = np.dot(df1.iloc[i], df2.iloc[i])
        sum_df1 = np.sum(df1.iloc[i])
        
        if sum_df1 != 0:
            forecast_aht = sumproduct / sum_df1
        else:
            forecast_aht = 0
        
        new_forecast_aht.append(forecast_aht)

    result2['Forecast AHT'] = new_forecast_aht
    result2
    return result2

    

def erlang_c_vectorized(A, N):
    A = np.atleast_1d(A)  # Ensure A is at least 1-dimensional
    N = np.atleast_1d(N)  # Ensure N is at least 1-dimensional
    with np.errstate(divide='ignore', invalid='ignore'):
        numerator = (A**N / factorial(N)) * (N / (N - A))
        denominator = np.sum((A[:, None]**np.arange(N + 1)) / factorial(np.arange(N + 1)), axis=1) + numerator
        E = numerator / denominator
        E[np.isnan(E)] = 1  # Handle the case where N <= A
        return E

def required_agents_vectorized(inflow, aht, sla, concurrencia, max_agents=200):
    A = (inflow/concurrencia) * (aht / 60)  # Calculate traffic intensity
    N = np.maximum(np.ceil(A).astype(int), 1)  # Minimum number of agents is 1
    
    all_agents = np.arange(1, max_agents + 1)
    
    def service_level(E, A, N):
        return (1 - E) * (1 - (A / N)) * 100
    
    required_agents = np.zeros_like(A, dtype=int)
    for i in range(len(A)):
        for agents in all_agents:
            E = erlang_c_vectorized(A[i], agents)
            current_service_level = service_level(E, A[i], agents)
            if current_service_level >= sla * 100:
                required_agents[i] = agents
                break
        if required_agents[i] == 0:
            required_agents[i] = max_agents  # If no solution found within max_agents, assign max_agents
    
    return required_agents

def hc(result,result2,sla, concurrencia):
    # Assuming result and result2 are DataFrames containing the relevant data
    df_inflow = result.drop(columns=['FECHA', 'Día', 'Forecast Inflow'])
    df_aht = result2.drop(columns=['FECHA', 'Día', 'Forecast AHT'])

    required_headcount_df = result[['FECHA', 'Día']].copy()
    required_headcount = np.zeros((df_inflow.shape[0], df_inflow.shape[1]), dtype=int)

    for i in range(len(df_inflow)):
        inflow_row = df_inflow.iloc[i].values
        aht_row = df_aht.iloc[i].values
        required_headcount[i] = required_agents_vectorized(inflow_row, aht_row, sla, concurrencia)

    required_headcount_df = pd.concat([required_headcount_df, pd.DataFrame(required_headcount, columns=df_inflow.columns)], axis=1)
    required_headcount_df.reset_index(drop=True, inplace=True)
    return required_headcount_df