# Exploratory Data Analysis Findings

Dataset period:

2016-01-01 → 2021-02-20

Total sales rows: 62,884
Customers: 15,266
Products: 2,517
Stores: 67

---

# Analysis Objectives

The exploratory analysis focuses on understanding:

* customer demographics
* product portfolio structure
* revenue trends
* channel performance
* geographic distribution
* store network efficiency

---

# Sections

1. Customer analysis
2. Product analysis
3. Sales analysis
4. Store analysis
5. Revenue deep dive
6. Premium product analysis
7. Store performance analysis

---

## 1. Customers

### Demographics
- Age ranges from 25 to 90 with a near-uniform distribution — no dominant age cluster.
- Under-25 customers represent just 1% of the base — the business has almost no younger audience.
- 65+ is the largest segment at 39%, followed by 50-64 and 35-49 at 22% each.
- Gender is near-perfectly balanced — Male 50.8%, Female 49.2%.

### Geography
- Business operates in 3 continents — North America, Europe, Australia.
- No presence in Asia, Africa, or South America.
- US dominates with 6,828 customers — more than the next 7 countries combined.
- UK (1,944) and Canada (1,553) are the only other countries with meaningful scale.

---

## 2. Products

### Catalogue
- 2,517 products across 8 categories.
- Home Appliances (26%) and Computers (24%) make up half the catalogue.
- Computer Accessories is the largest subcategory at 201 products.
- Contoso leads on volume (710 products), A. Datum leads on margin (58.13%).

### Pricing and Margin
- Margins are tight across all categories — range of 52-58%, suggesting a company-wide pricing policy.
- Margin distribution is bimodal — clusters at ~49% and ~54%, with a small cluster at 66-67%.
- Prices are strongly right-skewed — most products under $500, tail extending to $3,199.
- 200 products (7.95%) flagged as Premium (Unit Price > $921.50) — high-end desktops and TVs.

---

## 3. Sales

### Revenue Trend
- Revenue grew from $7.2M (2016) to a peak of $18.6M (2019) — 157% growth over 3 years.
- 2018 was the strongest growth year at +73.45%.
- Sharp decline from 2020 onward — down 49% in 2020, dataset ends February 2021.
- Q4 is consistently the strongest quarter every year. Q2 is consistently the weakest.
- Holiday/end-of-year purchasing is a clear seasonal driver.

### Channel
| Channel | Orders | Revenue | Avg Order Value |
|---------|--------|---------|-----------------|
| In-Store | 49,719 (79%) | $45.9M (80%) | $922 |
| Online | 13,165 (21%) | $11.7M (20%) | $886 |

- Business is predominantly physical — 66 stores vs 1 online storefront.
- Average order value is nearly identical across channels — channel does not influence spend.

### Delivery (Online Orders)
- 13,083 completed online deliveries. 82 pending at dataset cutoff.
- Mean delivery time: 4.53 days. 75% delivered within 6 days. Max: 17 days.
- No failed or negative delivery times — clean performance data.

### Geography
- US generates $29.9M — more than all other countries combined.
- UK second at $9.2M, Germany third at $6.1M.
- Australia and France underperform relative to their customer and store counts.

### Products
- Computers dominate revenue at $19.9M — nearly double Home Appliances ($11.1M).
- Top 10 products by revenue are all desktop PCs and large-screen TVs.
- Games and Toys weakest category at $747K.

---

## 4. Stores

### Network
- 66 physical stores across 8 countries, 1 online store (StoreKey 0).
- US has 24 stores — more than all European countries combined.
- Network was built between 2003 and 2008. No meaningful expansion since.
- StoreKey 0 identified as online store — only entry with null Square Meters.

### Revenue
| Channel | Revenue | Store Count | Avg per Store |
|---------|---------|-------------|---------------|
| Physical | $45.9M | 66 | ~$695K |
| Online (StoreKey 0) | $11.7M | 1 | $11.7M |

- Online store is 17x more productive per storefront than the average physical store.

### Store Size
- Two distinct formats — large (~2,000 sq m) concentrated in US and UK, small (~300-400 sq m) in France.
- UK average: 1,800 sq m. France average: 341 sq m — less than a quarter of UK.
- Store size has a weak positive relationship with revenue — location matters more than floor space.
- One store (~650 sq m) shows near-zero revenue across the full dataset — flagged for investigation.

### Top Stores
- Top 20 physical stores cluster between $1.1M and $1.4M — consistent performance across the network.

---

## 5. Revenue Deep Dive

### By Customer Segment
- 65+ drives $22.2M — nearly double the next age group and 38% of total revenue.
- Gender split is negligible — Male $29.2M vs Female $28.3M.
- North America 58%, Europe 38%, Australia 3% of total revenue.

### Average Order Value by Country
| Country | AOV |
|---------|-----|
| United Kingdom | $1,133 |
| Italy | $1,044 |
| Germany | $1,032 |
| France | $994 |
| Netherlands | $990 |
| United States | $885 |
| Canada | $664 |
| Australia | $661 |

- European customers spend significantly more per order than North American or Australian customers.
- US dominates total revenue through volume, not order size.

### Product Segments
- Premium products (7.95% of catalogue) generate $16.2M — 28% of total revenue.
- Standard products generate $41.4M — 72% of total revenue.
- Bulk orders (2.88% of orders) contribute $5.2M — 9% of revenue. Not a primary driver.

---

## Key Observations

| Area | Observation |
|------|-------------|
| Customer base | Heavily skewed toward 65+. Under-25 is virtually absent. |
| Geography | Concentrated in US and Europe. Australia underperforms. No Asia/Africa/South America. |
| Channel | Physical-first business but online is 17x more efficient per storefront. |
| Seasonality | Q4 spike every year. Q2 consistently weakest. |
| Products | Computers and premium SKUs drive disproportionate revenue. |
| Store network | Aging network (13-18 years old). Large variance in store performance at same size. |
| Decline | Steep revenue drop from 2020 — likely external disruption. Dataset ends before recovery. |