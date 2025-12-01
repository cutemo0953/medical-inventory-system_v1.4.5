-- HC Template: 衛生所 (Health Center)
-- 站點 ID: {{STATION_ID}}

-- 常用藥品
INSERT OR IGNORE INTO items (item_code, item_name, unit, min_stock, category) VALUES
('MED-001', 'Acetaminophen 500mg', 'Tab', 500, '常用藥品'),
('MED-002', 'Ibuprofen 400mg', 'Tab', 300, '常用藥品'),
('MED-003', 'Amoxicillin 500mg', 'Cap', 200, '常用藥品'),
('MED-004', 'Cefalexin 500mg', 'Cap', 200, '常用藥品'),
('MED-005', 'Metronidazole 250mg', 'Tab', 200, '常用藥品'),
('MED-006', 'Omeprazole 20mg', 'Cap', 200, '常用藥品'),
('MED-007', 'Loperamide 2mg', 'Tab', 100, '常用藥品'),
('MED-008', 'ORS 口服電解質', '包', 200, '常用藥品'),
('MED-009', 'Diphenhydramine 25mg', 'Tab', 100, '常用藥品'),
('MED-010', 'Prednisone 5mg', 'Tab', 100, '常用藥品');

-- 外傷耗材
INSERT OR IGNORE INTO items (item_code, item_name, unit, min_stock, category) VALUES
('WND-001', '無菌紗布 4x4', '包', 100, '外傷耗材'),
('WND-002', '彈性繃帶 3吋', '捲', 50, '外傷耗材'),
('WND-003', '彈性繃帶 4吋', '捲', 50, '外傷耗材'),
('WND-004', '透氣膠帶', '捲', 50, '外傷耗材'),
('WND-005', '生理食鹽水 250ml', '瓶', 50, '外傷耗材'),
('WND-006', '優碘溶液 250ml', '瓶', 20, '外傷耗材'),
('WND-007', '棉棒', '包', 100, '外傷耗材'),
('WND-008', 'OK繃 (綜合)', '盒', 30, '外傷耗材'),
('WND-009', '三角巾', 'EA', 20, '外傷耗材'),
('WND-010', '夾板 (小)', 'EA', 10, '外傷耗材');

-- 防護用品
INSERT OR IGNORE INTO items (item_code, item_name, unit, min_stock, category) VALUES
('PPE-001', '醫療口罩', '盒', 50, '防護用品'),
('PPE-002', 'N95口罩', '盒', 20, '防護用品'),
('PPE-003', '乳膠手套 M', '盒', 30, '防護用品'),
('PPE-004', '乳膠手套 L', '盒', 30, '防護用品'),
('PPE-005', '隔離衣', 'EA', 50, '防護用品'),
('PPE-006', '護目鏡', 'EA', 20, '防護用品');

-- 預設設備
INSERT OR IGNORE INTO equipment (id, name, category, quantity, status) VALUES
('EQ-001', '血壓計', '診斷設備', 3, 'UNCHECKED'),
('EQ-002', '體溫計', '診斷設備', 5, 'UNCHECKED'),
('EQ-003', '血氧機', '診斷設備', 3, 'UNCHECKED'),
('EQ-004', '診療床', '診療設備', 2, 'UNCHECKED'),
('EQ-005', '急救箱', '急救設備', 2, 'UNCHECKED');
