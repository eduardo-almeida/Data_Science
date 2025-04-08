-- Databricks notebook source
-- CREATE TABLE sandbox.analystics_churn_model.fs_vendedor_cliente AS

WITH tbl_clients AS (
  SELECT DISTINCT
    t1.idPedido,
    t1.idCliente,
    t2.idVendedor,
    t3.descUF
  FROM 
    silver.olist.pedido AS t1
  LEFT JOIN 
    silver.olist.item_pedido as t2
      ON t1.idPedido = t2.idPedido
  LEFT JOIN 
    silver.olist.cliente t3 
      ON t1.idCliente = t3.idCliente 
  WHERE 
    t1.dtPedido < '2018-01-01'
  AND 
    t1.dtPedido >= ADD_MONTHS('2018-01-01', -6)
  AND 
    idVendedor IS NOT NULL), 

tbl_pedidos_clients (
SELECT 
  idVendedor, 
  descUF,
  COUNT(DISTINCT idPedido) AS TotalPedidos, 
  COUNT(DISTINCT idCliente) AS TotalClients 
FROM 
  tbl_clients 
GROUP BY 
  idVendedor, 
  descUF
) 

SELECT 
  '2018-01-01' AS DateRef, 
  IdVendedor, 
  COUNT(DISTINCT descUF) AS QtyDistinctUFsPedidos, 
  SUM(TotalPedidos) AS TotalPedidos, 
  SUM(CASE WHEN descUF = 'SC' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_SC,
  SUM(CASE WHEN descUF = 'RO' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_RO,
  SUM(CASE WHEN descUF = 'PI' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_PI,
  SUM(CASE WHEN descUF = 'AM' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_AM,
  SUM(CASE WHEN descUF = 'RR' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_RR,
  SUM(CASE WHEN descUF = 'GO' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_GO,
  SUM(CASE WHEN descUF = 'TO' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_TO,
  SUM(CASE WHEN descUF = 'MT' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_MT,
  SUM(CASE WHEN descUF = 'SP' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_SP,
  SUM(CASE WHEN descUF = 'ES' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_ES,
  SUM(CASE WHEN descUF = 'PB' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_PB,
  SUM(CASE WHEN descUF = 'RS' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_RS,
  SUM(CASE WHEN descUF = 'MS' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_MS,
  SUM(CASE WHEN descUF = 'AL' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_AL,
  SUM(CASE WHEN descUF = 'MG' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_MG,
  SUM(CASE WHEN descUF = 'PA' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_PA,
  SUM(CASE WHEN descUF = 'BA' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_BA,
  SUM(CASE WHEN descUF = 'SE' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_SE,
  SUM(CASE WHEN descUF = 'PE' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_PE,
  SUM(CASE WHEN descUF = 'CE' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_CE,
  SUM(CASE WHEN descUF = 'RN' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_RN,
  SUM(CASE WHEN descUF = 'RJ' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_RJ,
  SUM(CASE WHEN descUF = 'MA' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_MA,
  SUM(CASE WHEN descUF = 'AC' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_AC,
  SUM(CASE WHEN descUF = 'DF' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_DF,
  SUM(CASE WHEN descUF = 'PR' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_PR,
  SUM(CASE WHEN descUF = 'AP' THEN TotalPedidos ELSE 0 END) / SUM(TotalPedidos) AS TotalPedidos_AP
FROM 
  tbl_pedidos_clients
GROUP BY 
  IdVendedor

-- COMMAND ----------

-- WITH tbl_clients AS (
--   SELECT DISTINCT
--     t1.idPedido,
--     t1.idCliente,
--     t2.idVendedor,
--     t3.descUF
--   FROM 
--     silver.olist.pedido AS t1
--   LEFT JOIN 
--     silver.olist.item_pedido as t2
--       ON t1.idPedido = t2.idPedido
--   LEFT JOIN 
--     silver.olist.cliente t3 
--       ON t1.idCliente = t3.idCliente 
--   WHERE 
--     t1.dtPedido < '2018-01-01'
--   AND 
--     t1.dtPedido >= ADD_MONTHS('2018-01-01', -6)
--   AND 
--     idVendedor IS NOT NULL), 

-- tbl_pedidos_clients (
-- SELECT 
--   idVendedor, 
--   descUF,
--   COUNT(DISTINCT idPedido) AS TotalPedidos, 
--   COUNT(DISTINCT idCliente) AS TotalClients 
-- FROM 
--   tbl_clients 
-- GROUP BY 
--   idVendedor, 
--   descUF
-- ) 

-- SELECT 
--   *, 
--   TotalPedidos / 70
-- FROM 
-- tbl_pedidos_clients
-- WHERE 
--   idVendedor = '0ea22c1cfbdc755f86b9b54b39c16043'
