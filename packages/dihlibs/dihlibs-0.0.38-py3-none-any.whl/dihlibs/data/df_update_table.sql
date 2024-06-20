WITH temp AS (
    SELECT * FROM ( VALUES
     {values}
    ) AS t({columns})
)
UPDATE {tablename} AS u_table
SET 
    {set_columns}
FROM temp
WHERE u_table.{id_column}=temp.{id_column} ;
WITH temp AS (
    SELECT * FROM ( VALUES
     {values}
    ) AS t({columns})
)
INSERT INTO {tablename} ({columns})
SELECT {update_columns} 
FROM temp
LEFT JOIN {tablename} AS u_table ON u_table.{id_column} = temp.{id_column}
WHERE u_table.{id_column} IS NULL;


INSERT INTO chv_p4p_snapshot ()
SELECT {update_columns} 
FROM chv_p4p
LEFT JOIN chv_p4p_snapshot AS snap using (chv_uuid,reported_month)
WHERE snap.chv_uuid IS NULL;
AND reported_month=date_trunc('month',current_date - interval  '1 month')