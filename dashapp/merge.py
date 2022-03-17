import pandas as pd

#pip install pandasql
from pandasql import sqldf

def pre_data():
    cl = pd.read_csv('~/UW/WIN22/CEE412/project/dashboard/data/Countylist.csv')

    # ac_cor_17_wc = pd.merge(left = ac_cor_17, right=cl, how = 'left', left_on = "COUNTY", right_on="COUNTY")
    # ac_cor_16_wc = pd.merge(left = ac_cor_16, right=cl, how = 'left', left_on = "COUNTY", right_on="COUNTY")
    # ac_cor_15_wc = pd.merge(left = ac_cor_15, right=cl, how = 'left', left_on = "COUNTY", right_on="COUNTY")
    # ac_cor_14_wc = pd.merge(left = ac_cor_14, right=cl, how = 'left', left_on = "COUNTY", right_on="COUNTY")
    # ac_cor_13_wc = pd.merge(left = ac_cor_13, right=cl, how = 'left', left_on = "COUNTY", right_on="COUNTY")
   
    acc_rd_list = []

    for i in ['13','14','15','16','17']:
        road_data = pd.read_csv('~/UW/WIN22/CEE412/project/dashboard/data/hsis-csv/wa{}road.csv'.format(i))
        acc_data = pd.read_csv('~/UW/WIN22/CEE412/project/dashboard/data/hsis-csv/wa{}acc.csv'.format(i))
        acc_data_wc = pd.merge(left = acc_data, right=cl, how = 'left', left_on = "COUNTY", right_on="COUNTY")
        pysqldf = lambda q: sqldf(q, globals())
        cond_join= '''
            SELECT 
                acc.* , rd.*
            FROM acc_data_wc AS acc
            LEFT JOIN road_data AS rd
            ON 
            (acc.rd_inv = rd.ROAD_INV) AND (acc.milepost >= rd.BEGMP) AND (acc.milepost < rd.ENDMP)
        '''
        # Now, get your queries results as dataframe using the sqldf object that you created
        acc_rd_wc = pysqldf(cond_join)
        acc_rd_wc.to_csv('../data/acc_rd_wc{}'.format(i),index=False)
        acc_rd_list.append(acc_rd_wc)

    #acc_rd_wc = pd.concat(acc_rd_list)
    return acc_rd_wc

pre_data()

    #acc_data = pd.read_csv('data/hsis-csv/wa{}acc.csv'.format(i))
    #veh_data = pd.read_csv('data/hsis-csv/wa{}veh.csv'.format(i))
    #occ_data = pd.read_csv('data/hsis-csv/wa{}occ.csv'.format(i))
    #acc_data.merge(veh_data, on = 'CASENO', how ='left')

    # acc_veh_all = acc_data.merge(veh_data, on = 'CASENO', how ='left')
    # acc_veh_all.drop_duplicates(['CASENO'], inplace = True)

    # acc_veh_all.to_csv("acc_veh_all{}.csv".format(i),index=False)

    #
    # Write your query in SQL syntax, here you can use df as a normal SQL table

