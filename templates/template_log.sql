-- LOG-HUB Template: 物資中心 (Logistic Hub)
-- 站點 ID: {{STATION_ID}}

-- 物資中心預設為空，主要用於接收和配送
-- 僅建立基本設備

INSERT OR IGNORE INTO equipment (id, name, category, quantity, status) VALUES
('EQ-001', '棧板推車', '搬運設備', 5, 'UNCHECKED'),
('EQ-002', '手推車', '搬運設備', 10, 'UNCHECKED'),
('EQ-003', '條碼掃描器', '資訊設備', 5, 'UNCHECKED'),
('EQ-004', '冷藏櫃', '冷鏈設備', 2, 'UNCHECKED'),
('EQ-005', '發電機', '電力設備', 1, 'UNCHECKED');
