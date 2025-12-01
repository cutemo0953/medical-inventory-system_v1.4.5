#!/usr/bin/env python3
"""
MIRS v1.4.2-plus - 預載資料庫
依據「急救站設置參考指引公開版本.pdf」衛生福利部建議清單
統一預載所有藥品/設備/耗材，不區分站點類型
"""

# ============================================================================
# 藥品預載清單 (pharmaceuticals table)
# ============================================================================

PHARMACEUTICALS_DATA = [
    # ========== 急救藥品 (18種) - 附件四 ==========
    {'code': 'EMER-001', 'name': 'Epinephrine 1:1000', 'generic_name': 'Epinephrine', 'unit': 'Amp', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-002', 'name': 'Atropine 1mg/ml', 'generic_name': 'Atropine', 'unit': 'Amp', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-003', 'name': 'Amiodarone 150mg', 'generic_name': 'Amiodarone', 'unit': 'Amp', 'min_stock': 10, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-004', 'name': 'Adenosine 6mg', 'generic_name': 'Adenosine', 'unit': 'Amp', 'min_stock': 10, 'category': '急救藥品', 'storage_condition': '冷藏', 'controlled_level': '非管制'},
    {'code': 'EMER-005', 'name': 'Lidocaine 2%', 'generic_name': 'Lidocaine', 'unit': 'Vial', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-006', 'name': 'Calcium Gluconate 10%', 'generic_name': 'Calcium Gluconate', 'unit': 'Amp', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-007', 'name': 'Sodium Bicarbonate 8.4%', 'generic_name': 'Sodium Bicarbonate', 'unit': 'Amp', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-008', 'name': 'Dextrose 50%', 'generic_name': 'Dextrose', 'unit': 'Amp', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-009', 'name': 'Naloxone 0.4mg', 'generic_name': 'Naloxone', 'unit': 'Amp', 'min_stock': 10, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-010', 'name': 'Flumazenil 0.5mg', 'generic_name': 'Flumazenil', 'unit': 'Amp', 'min_stock': 10, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-011', 'name': 'Vasopressin 20U', 'generic_name': 'Vasopressin', 'unit': 'Amp', 'min_stock': 10, 'category': '急救藥品', 'storage_condition': '冷藏', 'controlled_level': '非管制'},
    {'code': 'EMER-012', 'name': 'Dopamine 200mg', 'generic_name': 'Dopamine', 'unit': 'Amp', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-013', 'name': 'Norepinephrine 4mg', 'generic_name': 'Norepinephrine', 'unit': 'Amp', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-014', 'name': 'Dobutamine 250mg', 'generic_name': 'Dobutamine', 'unit': 'Vial', 'min_stock': 10, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-015', 'name': 'Hydrocortisone 100mg', 'generic_name': 'Hydrocortisone', 'unit': 'Vial', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-016', 'name': 'Diphenhydramine 30mg', 'generic_name': 'Diphenhydramine', 'unit': 'Amp', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-017', 'name': 'Nitroglycerin 0.6mg SL', 'generic_name': 'Nitroglycerin', 'unit': 'Tab', 'min_stock': 30, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'EMER-018', 'name': 'Aspirin 100mg', 'generic_name': 'Aspirin', 'unit': 'Tab', 'min_stock': 30, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},

    # ========== A. 止痛/消炎/退燒藥 - 附件六 ==========
    {'code': 'PAIN-001', 'name': 'Acetaminophen 500mg', 'generic_name': 'Acetaminophen', 'unit': 'Tab', 'min_stock': 200, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'PAIN-002', 'name': 'Ibuprofen 400mg', 'generic_name': 'Ibuprofen', 'unit': 'Tab', 'min_stock': 100, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'PAIN-003', 'name': 'Diclofenac 25mg', 'generic_name': 'Diclofenac', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'PAIN-004', 'name': 'Ketorolac 30mg/ml', 'generic_name': 'Ketorolac', 'unit': 'Amp', 'min_stock': 30, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'PAIN-005', 'name': 'Tramadol 50mg', 'generic_name': 'Tramadol', 'unit': 'Cap', 'min_stock': 50, 'category': '管制藥品', 'storage_condition': '常溫', 'controlled_level': '四級'},
    {'code': 'PAIN-006', 'name': 'Morphine 10mg/ml', 'generic_name': 'Morphine', 'unit': 'Amp', 'min_stock': 20, 'category': '管制藥品', 'storage_condition': '常溫', 'controlled_level': '二級'},
    {'code': 'PAIN-007', 'name': 'Meperidine 50mg/ml', 'generic_name': 'Meperidine', 'unit': 'Amp', 'min_stock': 20, 'category': '管制藥品', 'storage_condition': '常溫', 'controlled_level': '二級'},
    {'code': 'PAIN-008', 'name': 'Fentanyl 25mcg/hr Patch', 'generic_name': 'Fentanyl', 'unit': 'Patch', 'min_stock': 10, 'category': '管制藥品', 'storage_condition': '常溫', 'controlled_level': '二級'},
    {'code': 'PAIN-009', 'name': 'Nalbuphine 10mg/ml', 'generic_name': 'Nalbuphine', 'unit': 'Amp', 'min_stock': 20, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'PAIN-010', 'name': 'Celecoxib 200mg', 'generic_name': 'Celecoxib', 'unit': 'Cap', 'min_stock': 30, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},

    # ========== B. 呼吸道用藥 ==========
    {'code': 'RESP-001', 'name': 'Salbutamol MDI 100mcg', 'generic_name': 'Salbutamol', 'unit': 'Inh', 'min_stock': 10, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'RESP-002', 'name': 'Ipratropium MDI 20mcg', 'generic_name': 'Ipratropium', 'unit': 'Inh', 'min_stock': 10, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'RESP-003', 'name': 'Aminophylline 250mg/10ml', 'generic_name': 'Aminophylline', 'unit': 'Amp', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'RESP-004', 'name': 'Dextromethorphan 15mg', 'generic_name': 'Dextromethorphan', 'unit': 'Tab', 'min_stock': 100, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'RESP-005', 'name': 'Ambroxol 30mg', 'generic_name': 'Ambroxol', 'unit': 'Tab', 'min_stock': 100, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'RESP-006', 'name': 'Pseudoephedrine 60mg', 'generic_name': 'Pseudoephedrine', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'RESP-007', 'name': 'Chlorpheniramine 4mg', 'generic_name': 'Chlorpheniramine', 'unit': 'Tab', 'min_stock': 100, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'RESP-008', 'name': 'Montelukast 10mg', 'generic_name': 'Montelukast', 'unit': 'Tab', 'min_stock': 30, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'RESP-009', 'name': 'Budesonide 0.5mg/2ml Neb', 'generic_name': 'Budesonide', 'unit': 'Amp', 'min_stock': 20, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},

    # ========== C. 腸胃道用藥 ==========
    {'code': 'GI-001', 'name': 'Omeprazole 20mg', 'generic_name': 'Omeprazole', 'unit': 'Cap', 'min_stock': 100, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'GI-002', 'name': 'Ranitidine 150mg', 'generic_name': 'Ranitidine', 'unit': 'Tab', 'min_stock': 100, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'GI-003', 'name': 'Metoclopramide 10mg', 'generic_name': 'Metoclopramide', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'GI-004', 'name': 'Domperidone 10mg', 'generic_name': 'Domperidone', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'GI-005', 'name': 'Loperamide 2mg', 'generic_name': 'Loperamide', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'GI-006', 'name': 'Bisacodyl 5mg', 'generic_name': 'Bisacodyl', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'GI-007', 'name': 'Magnesium Oxide 250mg', 'generic_name': 'Magnesium Oxide', 'unit': 'Tab', 'min_stock': 100, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'GI-008', 'name': 'Simethicone 40mg', 'generic_name': 'Simethicone', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'GI-009', 'name': 'ORS 口服電解質', 'generic_name': 'Oral Rehydration Salts', 'unit': 'Pkt', 'min_stock': 100, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'GI-010', 'name': 'Ondansetron 4mg/2ml', 'generic_name': 'Ondansetron', 'unit': 'Amp', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'GI-011', 'name': 'Pantoprazole 40mg', 'generic_name': 'Pantoprazole', 'unit': 'Vial', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},

    # ========== D. 心臟血管用藥 ==========
    {'code': 'CV-001', 'name': 'Amlodipine 5mg', 'generic_name': 'Amlodipine', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'CV-002', 'name': 'Atenolol 50mg', 'generic_name': 'Atenolol', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'CV-003', 'name': 'Captopril 25mg', 'generic_name': 'Captopril', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'CV-004', 'name': 'Furosemide 40mg', 'generic_name': 'Furosemide', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'CV-005', 'name': 'Furosemide 20mg/2ml', 'generic_name': 'Furosemide', 'unit': 'Amp', 'min_stock': 30, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'CV-006', 'name': 'Hydrochlorothiazide 25mg', 'generic_name': 'Hydrochlorothiazide', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'CV-007', 'name': 'Spironolactone 25mg', 'generic_name': 'Spironolactone', 'unit': 'Tab', 'min_stock': 30, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'CV-008', 'name': 'Digoxin 0.25mg', 'generic_name': 'Digoxin', 'unit': 'Tab', 'min_stock': 30, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},

    # ========== E. 神經/精神用藥 ==========
    {'code': 'NEURO-001', 'name': 'Diazepam 5mg', 'generic_name': 'Diazepam', 'unit': 'Tab', 'min_stock': 30, 'category': '管制藥品', 'storage_condition': '常溫', 'controlled_level': '四級'},
    {'code': 'NEURO-002', 'name': 'Diazepam 10mg/2ml', 'generic_name': 'Diazepam', 'unit': 'Amp', 'min_stock': 20, 'category': '管制藥品', 'storage_condition': '常溫', 'controlled_level': '四級'},
    {'code': 'NEURO-003', 'name': 'Lorazepam 1mg', 'generic_name': 'Lorazepam', 'unit': 'Tab', 'min_stock': 30, 'category': '管制藥品', 'storage_condition': '常溫', 'controlled_level': '四級'},
    {'code': 'NEURO-004', 'name': 'Phenytoin 100mg', 'generic_name': 'Phenytoin', 'unit': 'Cap', 'min_stock': 30, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'NEURO-005', 'name': 'Haloperidol 5mg', 'generic_name': 'Haloperidol', 'unit': 'Tab', 'min_stock': 20, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'NEURO-006', 'name': 'Haloperidol 5mg/ml', 'generic_name': 'Haloperidol', 'unit': 'Amp', 'min_stock': 10, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},

    # ========== F. 抗生素 ==========
    {'code': 'ANTI-001', 'name': 'Amoxicillin 500mg', 'generic_name': 'Amoxicillin', 'unit': 'Cap', 'min_stock': 100, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'ANTI-002', 'name': 'Amoxicillin/Clavulanate 1g', 'generic_name': 'Amoxicillin/Clavulanate', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'ANTI-003', 'name': 'Cephalexin 500mg', 'generic_name': 'Cephalexin', 'unit': 'Cap', 'min_stock': 100, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'ANTI-004', 'name': 'Ceftriaxone 1g', 'generic_name': 'Ceftriaxone', 'unit': 'Vial', 'min_stock': 30, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'ANTI-005', 'name': 'Azithromycin 250mg', 'generic_name': 'Azithromycin', 'unit': 'Tab', 'min_stock': 30, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'ANTI-006', 'name': 'Ciprofloxacin 500mg', 'generic_name': 'Ciprofloxacin', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'ANTI-007', 'name': 'Metronidazole 250mg', 'generic_name': 'Metronidazole', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'ANTI-008', 'name': 'Gentamicin 80mg/2ml', 'generic_name': 'Gentamicin', 'unit': 'Amp', 'min_stock': 30, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},

    # ========== G. 血糖/血脂用藥 ==========
    {'code': 'ENDO-001', 'name': 'Metformin 500mg', 'generic_name': 'Metformin', 'unit': 'Tab', 'min_stock': 100, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'ENDO-002', 'name': 'Glibenclamide 5mg', 'generic_name': 'Glibenclamide', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'ENDO-003', 'name': 'Insulin Regular 100U/ml', 'generic_name': 'Insulin Regular', 'unit': 'Vial', 'min_stock': 5, 'category': '常用藥品', 'storage_condition': '冷藏', 'controlled_level': '非管制'},
    {'code': 'ENDO-004', 'name': 'Atorvastatin 20mg', 'generic_name': 'Atorvastatin', 'unit': 'Tab', 'min_stock': 50, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},

    # ========== H. 外傷用藥 ==========
    {'code': 'WOUND-001', 'name': 'Tetanus Toxoid 0.5ml', 'generic_name': 'Tetanus Toxoid', 'unit': 'Vial', 'min_stock': 20, 'category': '常用藥品', 'storage_condition': '冷藏', 'controlled_level': '非管制'},
    {'code': 'WOUND-002', 'name': 'Lidocaine 2% 20ml', 'generic_name': 'Lidocaine', 'unit': 'Vial', 'min_stock': 50, 'category': '麻醉藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'WOUND-003', 'name': 'Silver Sulfadiazine 1% Cream', 'generic_name': 'Silver Sulfadiazine', 'unit': 'Tube', 'min_stock': 10, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'WOUND-004', 'name': 'Povidone-Iodine 10%', 'generic_name': 'Povidone-Iodine', 'unit': 'Btl', 'min_stock': 20, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'WOUND-005', 'name': 'Chlorhexidine 4%', 'generic_name': 'Chlorhexidine', 'unit': 'Btl', 'min_stock': 10, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'WOUND-006', 'name': 'Tranexamic Acid 500mg/5ml', 'generic_name': 'Tranexamic Acid', 'unit': 'Amp', 'min_stock': 30, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'WOUND-007', 'name': 'Vitamin K 10mg/ml', 'generic_name': 'Phytonadione', 'unit': 'Amp', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},

    # ========== I. 輸液 ==========
    {'code': 'IV-001', 'name': 'Normal Saline 0.9% 500ml', 'generic_name': 'Sodium Chloride', 'unit': 'Bag', 'min_stock': 100, 'category': '輸液', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'IV-002', 'name': 'Lactated Ringer 500ml', 'generic_name': 'Lactated Ringer', 'unit': 'Bag', 'min_stock': 50, 'category': '輸液', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'IV-003', 'name': 'Dextrose 5% 500ml', 'generic_name': 'Dextrose', 'unit': 'Bag', 'min_stock': 50, 'category': '輸液', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'IV-004', 'name': 'Normal Saline 0.9% 1000ml', 'generic_name': 'Sodium Chloride', 'unit': 'Bag', 'min_stock': 50, 'category': '輸液', 'storage_condition': '常溫', 'controlled_level': '非管制'},

    # ========== J. 兒科用藥 ==========
    {'code': 'PEDS-001', 'name': 'Acetaminophen Syr 24mg/ml', 'generic_name': 'Acetaminophen', 'unit': 'Btl', 'min_stock': 10, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'PEDS-002', 'name': 'Ibuprofen Syr 20mg/ml', 'generic_name': 'Ibuprofen', 'unit': 'Btl', 'min_stock': 10, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'PEDS-003', 'name': 'Amoxicillin Syr 25mg/ml', 'generic_name': 'Amoxicillin', 'unit': 'Btl', 'min_stock': 10, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'PEDS-004', 'name': 'Domperidone Syr 1mg/ml', 'generic_name': 'Domperidone', 'unit': 'Btl', 'min_stock': 5, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'PEDS-005', 'name': 'Salbutamol Syr 2mg/5ml', 'generic_name': 'Salbutamol', 'unit': 'Btl', 'min_stock': 5, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},

    # ========== K. 產科藥物 (BORP專用) ==========
    {'code': 'OB-001', 'name': 'Oxytocin 10U/ml', 'generic_name': 'Oxytocin', 'unit': 'Amp', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '冷藏', 'controlled_level': '非管制'},
    {'code': 'OB-002', 'name': 'Methylergonovine 0.2mg/ml', 'generic_name': 'Methylergonovine', 'unit': 'Amp', 'min_stock': 10, 'category': '急救藥品', 'storage_condition': '冷藏', 'controlled_level': '非管制'},
    {'code': 'OB-003', 'name': 'Magnesium Sulfate 50%', 'generic_name': 'Magnesium Sulfate', 'unit': 'Amp', 'min_stock': 20, 'category': '急救藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'OB-004', 'name': 'Misoprostol 200mcg', 'generic_name': 'Misoprostol', 'unit': 'Tab', 'min_stock': 20, 'category': '常用藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},

    # ========== L. 麻醉藥品 (BORP專用) ==========
    {'code': 'ANES-001', 'name': 'Propofol 200mg/20ml', 'generic_name': 'Propofol', 'unit': 'Vial', 'min_stock': 50, 'category': '麻醉藥品', 'storage_condition': '常溫', 'controlled_level': '四級'},
    {'code': 'ANES-002', 'name': 'Ketamine 500mg/10ml', 'generic_name': 'Ketamine', 'unit': 'Vial', 'min_stock': 30, 'category': '麻醉藥品', 'storage_condition': '常溫', 'controlled_level': '三級'},
    {'code': 'ANES-003', 'name': 'Midazolam 5mg/ml', 'generic_name': 'Midazolam', 'unit': 'Amp', 'min_stock': 30, 'category': '麻醉藥品', 'storage_condition': '常溫', 'controlled_level': '四級'},
    {'code': 'ANES-004', 'name': 'Fentanyl 0.1mg/2ml', 'generic_name': 'Fentanyl', 'unit': 'Amp', 'min_stock': 50, 'category': '麻醉藥品', 'storage_condition': '常溫', 'controlled_level': '二級'},
    {'code': 'ANES-005', 'name': 'Rocuronium 50mg/5ml', 'generic_name': 'Rocuronium', 'unit': 'Vial', 'min_stock': 30, 'category': '麻醉藥品', 'storage_condition': '冷藏', 'controlled_level': '非管制'},
    {'code': 'ANES-006', 'name': 'Atracurium 50mg/5ml', 'generic_name': 'Atracurium', 'unit': 'Amp', 'min_stock': 30, 'category': '麻醉藥品', 'storage_condition': '冷藏', 'controlled_level': '非管制'},
    {'code': 'ANES-007', 'name': 'Neostigmine 0.5mg/ml', 'generic_name': 'Neostigmine', 'unit': 'Amp', 'min_stock': 20, 'category': '麻醉藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'ANES-008', 'name': 'Sugammadex 200mg/2ml', 'generic_name': 'Sugammadex', 'unit': 'Vial', 'min_stock': 10, 'category': '麻醉藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'ANES-009', 'name': 'Bupivacaine 0.5% 20ml', 'generic_name': 'Bupivacaine', 'unit': 'Vial', 'min_stock': 30, 'category': '麻醉藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},
    {'code': 'ANES-010', 'name': 'Sevoflurane 250ml', 'generic_name': 'Sevoflurane', 'unit': 'Btl', 'min_stock': 5, 'category': '麻醉藥品', 'storage_condition': '常溫', 'controlled_level': '非管制'},

    # ========== M. 疫苗與免疫製劑 ==========
    {'code': 'VAC-001', 'name': 'Tetanus Immunoglobulin 250IU', 'generic_name': 'Tetanus Immunoglobulin', 'unit': 'Vial', 'min_stock': 10, 'category': '常用藥品', 'storage_condition': '冷藏', 'controlled_level': '非管制'},
]

# ============================================================================
# 設備預載清單 (equipment table)
# ============================================================================

EQUIPMENT_DATA = [
    # ========== 基礎水電維生設備 (附件五) ==========
    {'id': 'UTIL-001', 'name': '行動電源站', 'category': '電力設備', 'quantity': 1},
    {'id': 'UTIL-002', 'name': '發電機 (備用)', 'category': '電力設備', 'quantity': 1},
    {'id': 'UTIL-003', 'name': '光觸媒空氣清淨機', 'category': '空氣淨化', 'quantity': 1},
    {'id': 'UTIL-004', 'name': '淨水器 (RO)', 'category': '水處理', 'quantity': 1},
    {'id': 'UTIL-005', 'name': '行動冰箱', 'category': '冷藏設備', 'quantity': 2},
    {'id': 'UTIL-006', 'name': '醫療級冷凍櫃', 'category': '冷藏設備', 'quantity': 1},

    # ========== 一般醫療設備 (附件二) ==========
    {'id': 'DIAG-001', 'name': '血壓計 (電子式)', 'category': '診斷設備', 'quantity': 3},
    {'id': 'DIAG-002', 'name': '體溫計 (額溫槍)', 'category': '診斷設備', 'quantity': 5},
    {'id': 'DIAG-003', 'name': '血氧機 (指夾式)', 'category': '診斷設備', 'quantity': 3},
    {'id': 'DIAG-004', 'name': '聽診器', 'category': '診斷設備', 'quantity': 3},
    {'id': 'DIAG-005', 'name': '血糖機', 'category': '診斷設備', 'quantity': 2},
    {'id': 'DIAG-006', 'name': '12導程心電圖機', 'category': '診斷設備', 'quantity': 1},

    # ========== 急救設備 ==========
    {'id': 'EMER-EQ-001', 'name': 'AED 自動體外除顫器', 'category': '急救設備', 'quantity': 1},
    {'id': 'EMER-EQ-002', 'name': '甦醒球 (成人)', 'category': '急救設備', 'quantity': 2},
    {'id': 'EMER-EQ-003', 'name': '甦醒球 (兒童)', 'category': '急救設備', 'quantity': 1},
    {'id': 'EMER-EQ-004', 'name': '喉頭鏡組', 'category': '急救設備', 'quantity': 1},
    {'id': 'EMER-EQ-005', 'name': '氣管內管組', 'category': '急救設備', 'quantity': 1},
    {'id': 'EMER-EQ-006', 'name': '氧氣瓶 (E size)', 'category': '急救設備', 'quantity': 2},
    {'id': 'EMER-EQ-007', 'name': '抽吸機', 'category': '急救設備', 'quantity': 1},
    {'id': 'EMER-EQ-008', 'name': '脊椎固定板', 'category': '急救設備', 'quantity': 2},
    {'id': 'EMER-EQ-009', 'name': '頸圈 (各尺寸)', 'category': '急救設備', 'quantity': 5},

    # ========== BORP 手術器械包 ==========
    {'id': 'BORP-SURG-001', 'name': '共同基本包 (一)', 'category': '手術器械', 'quantity': 8},
    {'id': 'BORP-SURG-002', 'name': '共同基本包 (二)', 'category': '手術器械', 'quantity': 8},
    {'id': 'BORP-SURG-003', 'name': '骨科包', 'category': '手術器械', 'quantity': 8},
    {'id': 'BORP-SURG-004', 'name': '開腹輔助包', 'category': '手術器械', 'quantity': 8},
    {'id': 'BORP-SURG-005', 'name': '腹部開創器', 'category': '手術器械', 'quantity': 8},
    {'id': 'BORP-SURG-006', 'name': '開胸基本包', 'category': '手術器械', 'quantity': 1},
    {'id': 'BORP-SURG-007', 'name': '血管包', 'category': '手術器械', 'quantity': 3},
    {'id': 'BORP-SURG-008', 'name': '心外基本包', 'category': '手術器械', 'quantity': 4},
    {'id': 'BORP-SURG-009', 'name': 'ASSET包', 'category': '手術器械', 'quantity': 8},
    {'id': 'BORP-SURG-010', 'name': '皮膚縫合包', 'category': '手術器械', 'quantity': 2},
    {'id': 'BORP-SURG-011', 'name': '氣切輔助包', 'category': '手術器械', 'quantity': 8},
    {'id': 'BORP-SURG-012', 'name': 'Bull dog血管夾', 'category': '手術器械', 'quantity': 4},
    {'id': 'BORP-SURG-013', 'name': '顱骨手搖鑽', 'category': '手術器械', 'quantity': 1},
    {'id': 'BORP-SURG-014', 'name': '鑽/切骨電動工具組', 'category': '手術器械', 'quantity': 1},
    {'id': 'BORP-SURG-015', 'name': '電池式電動骨鑽', 'category': '手術器械', 'quantity': 1},
    {'id': 'BORP-SURG-016', 'name': '電池式電動骨鋸', 'category': '手術器械', 'quantity': 3},
]

# ============================================================================
# 耗材預載清單 (items table)
# ============================================================================

CONSUMABLES_DATA = [
    # ========== 紗布與敷料 ==========
    {'code': 'GAUZE-001', 'name': '無菌紗布 2x2', 'unit': '包', 'min_stock': 200, 'category': '敷料'},
    {'code': 'GAUZE-002', 'name': '無菌紗布 4x4', 'unit': '包', 'min_stock': 300, 'category': '敷料'},
    {'code': 'GAUZE-003', 'name': '無菌紗布 8x8', 'unit': '包', 'min_stock': 100, 'category': '敷料'},
    {'code': 'BAND-001', 'name': '彈性繃帶 2吋', 'unit': '捲', 'min_stock': 50, 'category': '敷料'},
    {'code': 'BAND-002', 'name': '彈性繃帶 3吋', 'unit': '捲', 'min_stock': 50, 'category': '敷料'},
    {'code': 'BAND-003', 'name': '彈性繃帶 4吋', 'unit': '捲', 'min_stock': 50, 'category': '敷料'},
    {'code': 'TAPE-001', 'name': '透氣膠帶 1吋', 'unit': '捲', 'min_stock': 50, 'category': '敷料'},
    {'code': 'TAPE-002', 'name': '透氣膠帶 2吋', 'unit': '捲', 'min_stock': 30, 'category': '敷料'},

    # ========== 注射用品 ==========
    {'code': 'SYR-001', 'name': '注射器 1ml', 'unit': '支', 'min_stock': 100, 'category': '注射用品'},
    {'code': 'SYR-002', 'name': '注射器 3ml', 'unit': '支', 'min_stock': 200, 'category': '注射用品'},
    {'code': 'SYR-003', 'name': '注射器 5ml', 'unit': '支', 'min_stock': 200, 'category': '注射用品'},
    {'code': 'SYR-004', 'name': '注射器 10ml', 'unit': '支', 'min_stock': 100, 'category': '注射用品'},
    {'code': 'SYR-005', 'name': '注射器 20ml', 'unit': '支', 'min_stock': 50, 'category': '注射用品'},
    {'code': 'NDL-001', 'name': '針頭 18G', 'unit': '支', 'min_stock': 100, 'category': '注射用品'},
    {'code': 'NDL-002', 'name': '針頭 20G', 'unit': '支', 'min_stock': 100, 'category': '注射用品'},
    {'code': 'NDL-003', 'name': '針頭 22G', 'unit': '支', 'min_stock': 100, 'category': '注射用品'},
    {'code': 'NDL-004', 'name': '針頭 25G', 'unit': '支', 'min_stock': 100, 'category': '注射用品'},

    # ========== 靜脈輸液用品 ==========
    {'code': 'IVC-001', 'name': '靜脈留置針 18G', 'unit': '支', 'min_stock': 50, 'category': '注射用品'},
    {'code': 'IVC-002', 'name': '靜脈留置針 20G', 'unit': '支', 'min_stock': 100, 'category': '注射用品'},
    {'code': 'IVC-003', 'name': '靜脈留置針 22G', 'unit': '支', 'min_stock': 100, 'category': '注射用品'},
    {'code': 'IVC-004', 'name': '靜脈留置針 24G', 'unit': '支', 'min_stock': 50, 'category': '注射用品'},
    {'code': 'IVSET-001', 'name': '點滴套組', 'unit': '組', 'min_stock': 100, 'category': '注射用品'},
    {'code': 'IVSET-002', 'name': '輸血套組', 'unit': '組', 'min_stock': 30, 'category': '注射用品'},
    {'code': 'EXT-001', 'name': '三向活栓', 'unit': '個', 'min_stock': 50, 'category': '注射用品'},

    # ========== 防護用品 ==========
    {'code': 'PPE-001', 'name': '外科口罩', 'unit': '盒', 'min_stock': 50, 'category': '防護用品'},
    {'code': 'PPE-002', 'name': 'N95口罩', 'unit': '盒', 'min_stock': 20, 'category': '防護用品'},
    {'code': 'PPE-003', 'name': '乳膠手套 M', 'unit': '盒', 'min_stock': 30, 'category': '防護用品'},
    {'code': 'PPE-004', 'name': '乳膠手套 L', 'unit': '盒', 'min_stock': 30, 'category': '防護用品'},
    {'code': 'PPE-005', 'name': '隔離衣', 'unit': '件', 'min_stock': 50, 'category': '防護用品'},
    {'code': 'PPE-006', 'name': '面罩', 'unit': '個', 'min_stock': 20, 'category': '防護用品'},
    {'code': 'PPE-007', 'name': '護目鏡', 'unit': '個', 'min_stock': 10, 'category': '防護用品'},

    # ========== 傷口處理 ==========
    {'code': 'CLEAN-001', 'name': '生理食鹽水 250ml', 'unit': '瓶', 'min_stock': 50, 'category': '清潔用品'},
    {'code': 'CLEAN-002', 'name': '優碘溶液', 'unit': '瓶', 'min_stock': 20, 'category': '清潔用品'},
    {'code': 'CLEAN-003', 'name': '75%酒精', 'unit': '瓶', 'min_stock': 30, 'category': '清潔用品'},
    {'code': 'CLEAN-004', 'name': '棉棒', 'unit': '包', 'min_stock': 100, 'category': '清潔用品'},
    {'code': 'CLEAN-005', 'name': '棉球', 'unit': '包', 'min_stock': 50, 'category': '清潔用品'},

    # ========== 縫合材料 ==========
    {'code': 'SUTURE-001', 'name': 'Vicryl 2-0', 'unit': '條', 'min_stock': 30, 'category': '手術耗材'},
    {'code': 'SUTURE-002', 'name': 'Vicryl 3-0', 'unit': '條', 'min_stock': 30, 'category': '手術耗材'},
    {'code': 'SUTURE-003', 'name': 'Vicryl 4-0', 'unit': '條', 'min_stock': 30, 'category': '手術耗材'},
    {'code': 'SUTURE-004', 'name': 'Nylon 3-0', 'unit': '條', 'min_stock': 30, 'category': '手術耗材'},
    {'code': 'SUTURE-005', 'name': 'Nylon 4-0', 'unit': '條', 'min_stock': 30, 'category': '手術耗材'},
    {'code': 'SUTURE-006', 'name': 'Silk 3-0', 'unit': '條', 'min_stock': 20, 'category': '手術耗材'},
]

# ============================================================================
# 預載函數
# ============================================================================

def get_all_preload_data():
    """取得所有預載資料"""
    return {
        'pharmaceuticals': PHARMACEUTICALS_DATA,
        'equipment': EQUIPMENT_DATA,
        'consumables': CONSUMABLES_DATA
    }


def get_pharmaceuticals_count():
    """取得藥品數量"""
    return len(PHARMACEUTICALS_DATA)


def get_equipment_count():
    """取得設備數量"""
    return len(EQUIPMENT_DATA)


def get_consumables_count():
    """取得耗材數量"""
    return len(CONSUMABLES_DATA)


if __name__ == '__main__':
    # 測試輸出
    print(f"藥品數量: {get_pharmaceuticals_count()}")
    print(f"設備數量: {get_equipment_count()}")
    print(f"耗材數量: {get_consumables_count()}")
    print(f"\n藥品分類統計:")
    categories = {}
    for p in PHARMACEUTICALS_DATA:
        cat = p['category']
        categories[cat] = categories.get(cat, 0) + 1
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}")
