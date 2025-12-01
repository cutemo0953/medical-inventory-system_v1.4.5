-- BORP Template: 備援手術室 (Backup Operating Room Point)
-- 站點 ID: {{STATION_ID}}

-- 手術耗材
INSERT OR IGNORE INTO items (item_code, item_name, unit, min_stock, category) VALUES
('SURG-001', '手術刀片 #10', 'EA', 20, '手術耗材'),
('SURG-002', '手術刀片 #15', 'EA', 20, '手術耗材'),
('SURG-003', '手術刀柄 #3', 'EA', 5, '手術耗材'),
('SURG-004', '可吸收縫線 3-0', 'EA', 50, '手術耗材'),
('SURG-005', '可吸收縫線 4-0', 'EA', 50, '手術耗材'),
('SURG-006', '不可吸收縫線 3-0', 'EA', 30, '手術耗材'),
('SURG-007', '無菌手套 6.5', '雙', 100, '手術耗材'),
('SURG-008', '無菌手套 7.0', '雙', 100, '手術耗材'),
('SURG-009', '無菌手套 7.5', '雙', 100, '手術耗材'),
('SURG-010', '手術衣 L', 'EA', 30, '手術耗材'),
('SURG-011', '手術衣 XL', 'EA', 30, '手術耗材'),
('SURG-012', '無菌紗布 4x4', '包', 200, '手術耗材'),
('SURG-013', '無菌紗布 2x2', '包', 200, '手術耗材'),
('SURG-014', '引流管 #10', 'EA', 20, '手術耗材'),
('SURG-015', '引流管 #14', 'EA', 20, '手術耗材'),
('SURG-016', '胸腔引流瓶', 'EA', 10, '手術耗材'),
('SURG-017', '骨蠟', 'EA', 20, '手術耗材'),
('SURG-018', '止血海綿', '片', 50, '手術耗材'),
('SURG-019', '電燒筆', 'EA', 10, '手術耗材'),
('SURG-020', '吸引管', 'EA', 20, '手術耗材');

-- 麻醉藥品
INSERT OR IGNORE INTO items (item_code, item_name, unit, min_stock, category) VALUES
('ANES-001', 'Propofol 200mg/20ml', 'Amp', 30, '麻醉藥品'),
('ANES-002', 'Ketamine 500mg/10ml', 'Vial', 20, '麻醉藥品'),
('ANES-003', 'Midazolam 5mg/ml', 'Amp', 30, '麻醉藥品'),
('ANES-004', 'Fentanyl 0.1mg/2ml', 'Amp', 50, '麻醉藥品'),
('ANES-005', 'Morphine 10mg/ml', 'Amp', 30, '麻醉藥品'),
('ANES-006', 'Lidocaine 2% 20ml', 'Vial', 50, '麻醉藥品'),
('ANES-007', 'Bupivacaine 0.5%', 'Vial', 30, '麻醉藥品'),
('ANES-008', 'Atropine 0.5mg/ml', 'Amp', 30, '麻醉藥品'),
('ANES-009', 'Epinephrine 1mg/ml', 'Amp', 30, '麻醉藥品'),
('ANES-010', 'Rocuronium 50mg/5ml', 'Vial', 20, '麻醉藥品');

-- 急救藥品
INSERT OR IGNORE INTO items (item_code, item_name, unit, min_stock, category) VALUES
('EMER-001', 'Epinephrine 1:1000', 'Amp', 20, '急救藥品'),
('EMER-002', 'Atropine 1mg', 'Amp', 20, '急救藥品'),
('EMER-003', 'Amiodarone 150mg', 'Amp', 10, '急救藥品'),
('EMER-004', 'Calcium Gluconate', 'Amp', 20, '急救藥品'),
('EMER-005', 'Sodium Bicarbonate', 'Amp', 20, '急救藥品'),
('EMER-006', 'Dextrose 50%', 'Amp', 20, '急救藥品'),
('EMER-007', 'Naloxone 0.4mg', 'Amp', 10, '急救藥品'),
('EMER-008', 'Flumazenil 0.5mg', 'Amp', 10, '急救藥品');

-- 輸液
INSERT OR IGNORE INTO items (item_code, item_name, unit, min_stock, category) VALUES
('IV-001', 'Normal Saline 500ml', '袋', 50, '輸液'),
('IV-002', 'Normal Saline 1000ml', '袋', 50, '輸液'),
('IV-003', 'Lactated Ringer 500ml', '袋', 30, '輸液'),
('IV-004', 'Lactated Ringer 1000ml', '袋', 30, '輸液'),
('IV-005', 'D5W 500ml', '袋', 20, '輸液'),
('IV-006', 'Gelofusine 500ml', '袋', 20, '輸液');

-- 預設設備
INSERT OR IGNORE INTO equipment (id, name, category, quantity, status) VALUES
('EQ-001', '麻醉機', '麻醉設備', 1, 'UNCHECKED'),
('EQ-002', '生理監視器', '監測設備', 2, 'UNCHECKED'),
('EQ-003', '電燒機', '手術設備', 1, 'UNCHECKED'),
('EQ-004', '吸引器', '手術設備', 2, 'UNCHECKED'),
('EQ-005', '無影燈', '手術設備', 2, 'UNCHECKED'),
('EQ-006', '手術床', '手術設備', 1, 'UNCHECKED'),
('EQ-007', '除顫器', '急救設備', 1, 'UNCHECKED'),
('EQ-008', '呼吸器', '呼吸設備', 1, 'UNCHECKED'),
('EQ-009', '輸液加溫器', '輸液設備', 2, 'UNCHECKED'),
('EQ-010', '行動電源站', '電力設備', 1, 'UNCHECKED');
