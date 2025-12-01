-- HOSP Template: 醫院自訂 (Hospital Custom)
-- 站點 ID: {{STATION_ID}}

-- 空白模板，由醫院自行設定
-- 僅建立範例設備

INSERT OR IGNORE INTO equipment (id, name, category, quantity, status) VALUES
('EQ-001', '範例設備', '其他', 1, 'UNCHECKED');
