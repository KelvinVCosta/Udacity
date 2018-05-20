SQL_ARTICLES_MOST_VIEWS = '''SELECT articles.title, COUNT(log.path)QTY_VIEWS 
                             FROM articles INNER JOIN log 
                             ON slug = replace(path, '/article/', '') 
                             WHERE log.status = '200 OK' 
                             GROUP BY articles.title 
                             ORDER BY QTY_VIEWS DESC LIMIT 3;'''

SQL_AUTHORS_MOST_VIEWS = '''SELECT authors.name, COUNT(log.path)QTY_VIEWS 
                            FROM articles INNER JOIN log 
                            ON slug = replace(path, '/article/', '') 
                            INNER JOIN authors ON articles.author = authors.id 
                            WHERE log.status = '200 OK' 
                            GROUP BY authors.name 
                            ORDER BY QTY_VIEWS DESC;'''

SQL_ERR_LOG_1_PERC_MORE = '''SELECT CAST(time as date) AS DATE, 
                             CAST(CAST(100 * SUM(CASE WHEN 
                             status = '404 NOT FOUND' THEN 1 ELSE 0 END) 
                             AS DECIMAL(10,2))/ SUM(CASE WHEN 
                             status IS NOT NULL THEN 1 ELSE 0 END)
                             AS DECIMAL(3,2)) AS PERCENTAGE,
                             SUM(CASE WHEN status = '404 NOT FOUND' 
                             THEN 1 ELSE 0 END) AS TOTAL_ERR,
                             SUM(CASE WHEN status IS NOT NULL THEN 1 ELSE 0 END) 
                             AS TOTAL_LOGS FROM log GROUP BY DATE 
                             HAVING CAST(SUM(CASE WHEN status = '404 NOT FOUND' 
                             THEN 1 ELSE 0 END) AS DECIMAL(10,2)) / SUM(CASE 
                             WHEN status IS NOT NULL THEN 1 ELSE 0 END) 
                             > 0.01 ORDER BY DATE'''