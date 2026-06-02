-- Total Sales

SELECT
ROUND(SUM(Sales),2) AS total_sales
FROM sales;


-- Total Profit

SELECT
ROUND(SUM(Profit),2) AS total_profit
FROM sales;


-- Sales By Region

SELECT
Region,
ROUND(SUM(Sales),2) AS sales
FROM sales
GROUP BY Region
ORDER BY sales DESC;


-- Profit By Category

SELECT
Category,
ROUND(SUM(Profit),2) AS profit
FROM sales
GROUP BY Category
ORDER BY profit DESC;


-- Top Customers

SELECT
Customer_Name,
ROUND(SUM(Sales),2) AS sales
FROM sales
GROUP BY Customer_Name
ORDER BY sales DESC
LIMIT 10;


-- Top States

SELECT
State,
ROUND(SUM(Sales),2) AS sales
FROM sales
GROUP BY State
ORDER BY sales DESC
LIMIT 10;