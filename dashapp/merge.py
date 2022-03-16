import pandas as pd

#pip install pandasql
from pandasql import sqldf


for i in ['13','14','15','16','17']:
    acc_data = pd.read_csv('../hsis-full/hsis-csv/wa{}acc.csv'.format(i))
    road_data = pd.read_csv('../hsis-full/hsis-csv/wa{}road.csv'.format(i))
    veh_data = pd.read_csv('../hsis-full/hsis-csv/wa{}veh.csv'.format(i))
    occ_data = pd.read_csv('../hsis-full/hsis-csv/wa{}occ.csv'.format(i))
    acc_data.merge(veh_data, on = 'CASENO', how ='left')

    acc_veh_all = acc_data.merge(veh_data, on = 'CASENO', how ='left')
    acc_veh_all.drop_duplicates(['CASENO'], inplace = True)

    acc_veh_all.to_csv("acc_veh_all{}.csv".format(i),index=False)

    pysqldf = lambda q: sqldf(q, globals())
    # Write your query in SQL syntax, here you can use df as a normal SQL table
    cond_join= '''
        SELECT 
            acc.* , rd.*
        FROM acc_data AS acc
        LEFT JOIN road_data AS rd
        ON 
        (acc.rd_inv = rd.ROAD_INV) AND (acc.milepost >= rd.BEGMP) AND (acc.milepost < rd.ENDMP)
    '''

    # Now, get your queries results as dataframe using the sqldf object that you created
    acc_rd = pysqldf(cond_join)
    acc_rd.to_csv("acc_rd{}.csv".format(i),index=False)