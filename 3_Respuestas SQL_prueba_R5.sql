-- ¿Cuáles son las tiendas con compras de al menos 100 clientes diferentes?
select codigo_tienda, 
count(distinct(num_documento_cliente)) as Cantidad_clientes
from `Prueba.Ventas` 
group by codigo_tienda
having count(distinct(num_documento_cliente))>=100
;
-- ¿Cuáles son los 5 barrios donde la mayor cantidad de clientes únicos realizan compras en tiendas tipo 'Tienda Regional'?
select nombre_barrio,
count(distinct(num_documento_cliente))  as Cantidad_clientes
from `Prueba.Ventas` 
where tipo_tienda='Tienda Regional'
group by nombre_barrio
order by count(distinct(num_documento_cliente))  desc
limit 5
;