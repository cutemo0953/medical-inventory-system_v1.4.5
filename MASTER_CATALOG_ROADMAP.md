# Master Catalog System - Implementation Roadmap

## 🎯 Vision

**Single-Station Model with Centralized Item Management**

Each MIRS instance serves ONE station, but all stations use the SAME standardized item codes from a master catalog. This ensures:
- ✅ No code conflicts between stations
- ✅ Consistent item naming (everyone calls "紗布 4x4" by the same code: `GAUZE-4X4`)
- ✅ Easy demos of different station types (health center vs surgical station vs logistics hub)
- ✅ Quality control (only approved items with proper specs)

---

## 📊 Current Status (v1.4.5)

### ✅ Completed
- Master catalog created with 100+ items (`database/master_catalog.sql`)
- Standardized code prefixes:
  - `PPE-` = Protective equipment
  - `GAUZE-`, `BAND-` = Wound care
  - `SYRINGE-`, `NEEDLE-`, `IV-` = Injection supplies
  - `MED-` = Medicines
  - `EQUIP-` = Equipment
  - `SURG-` = Surgical instruments
  - `DIAG-` = Diagnostic tools
  - `CLEAN-` = Disinfection/sanitation

### ⚠️ Current Issues
- Users can still create custom item codes (bypasses catalog)
- Station profiles manually duplicate item definitions
- No UI for browsing/selecting from catalog

---

## 🗺️ Implementation Phases

### **Phase 1: Backend Foundation** (Next Sprint)

**Goal:** Make catalog the single source of truth

#### 1.1 Disable Custom Code Creation
```python
# In main.py - Update create_item endpoint
@app.post("/api/items")
async def create_item(request: ItemCreateRequest):
    # OLD: if not request.code: item_code = db.generate_item_code(...)

    # NEW: Code must come from request (selected from catalog)
    if not request.code:
        raise HTTPException(400, "必須從目錄選擇物品，不可自行建立代碼")

    # Verify code exists in master catalog
    if not db.is_valid_catalog_code(request.code):
        raise HTTPException(400, f"無效的物品代碼: {request.code}")
```

#### 1.2 Add Catalog Query API
```python
@app.get("/api/catalog/search")
async def search_catalog(q: str = "", category: str = ""):
    """搜尋主目錄物品"""
    # Return items from master catalog that match search

@app.get("/api/catalog/categories")
async def get_categories():
    """取得所有分類"""
    return ["防護用品", "醫療耗材", "注射用品", "藥品", "手術器械", ...]
```

#### 1.3 Update Station Profiles
Convert profiles to SELECT from catalog instead of INSERT new items:

```sql
-- OLD (surgical_station.sql):
-- INSERT INTO items (item_code, item_name, ...) VALUES (...)

-- NEW:
.read database/master_catalog.sql

-- Mark selected items as active for this station type
UPDATE items SET
    is_active = 1,
    min_stock = 10,
    max_stock = 100
WHERE item_code IN (
    'SURG-ASSET-PKG',
    'SURG-SCALPEL-HANDLE',
    'PPE-GLOVE-M',
    ...
);
```

**Deliverables:**
- [ ] Modified `create_item` endpoint
- [ ] New catalog search APIs
- [ ] Updated all 4 station profiles to use SELECT model
- [ ] API tests

---

### **Phase 2: UI for Catalog Selection** (Sprint 2)

**Goal:** Replace "新增物品" with "從目錄新增"

#### 2.1 Catalog Browser Modal
```html
<!-- Replace current "新增物品" modal -->
<div x-show="showCatalogModal">
    <h3>從主目錄選擇物品</h3>

    <!-- Search & Filter -->
    <input type="text" x-model="catalogSearch"
           placeholder="搜尋物品名稱或代碼...">

    <select x-model="catalogCategory">
        <option value="">全部分類</option>
        <option>防護用品</option>
        <option>醫療耗材</option>
        <option>藥品</option>
        ...
    </select>

    <!-- Results Table -->
    <table>
        <tr x-for="item in filteredCatalogItems">
            <td x-text="item.item_code">PPE-GLOVE-M</td>
            <td x-text="item.item_name">醫療手套 Medium</td>
            <td x-text="item.specification">100入/盒</td>
            <td>
                <button @click="addItemFromCatalog(item)">
                    + 新增至庫存
                </button>
            </td>
        </tr>
    </table>
</div>
```

#### 2.2 Station Inventory Management
```javascript
async addItemFromCatalog(catalogItem) {
    // Add item to THIS station's active inventory
    const response = await fetch('/api/items/activate', {
        method: 'POST',
        body: JSON.stringify({
            item_code: catalogItem.item_code,
            min_stock: 10,  // Station manager sets thresholds
            max_stock: 100,
            current_stock: 0
        })
    });

    this.toast('已新增至庫存清單', 'success');
    this.loadItems();  // Refresh
}
```

**Deliverables:**
- [ ] Catalog browser modal UI
- [ ] Search/filter functionality
- [ ] "Add to inventory" workflow
- [ ] Remove old "新增物品" form

---

### **Phase 3: Admin Catalog Management** (Future)

**Goal:** Allow authorized users to update master catalog

#### 3.1 Catalog Admin UI (Future Feature)
- View all catalog items
- Add new standardized items
- Update specifications
- Retire obsolete items

#### 3.2 Catalog Versioning
```sql
-- Track catalog updates
CREATE TABLE catalog_updates (
    version TEXT,
    release_date DATE,
    changes TEXT,
    author TEXT
);
```

**Deliverables:**
- [ ] Admin panel (restricted access)
- [ ] Catalog CRUD operations
- [ ] Version control system

---

## 📋 Migration Plan

### How to Transition Existing Stations

**Option A: Fresh Start (Recommended for Demo)**
1. Delete existing database
2. Run setup wizard
3. Select station profile (loads from master catalog)
4. All items use standardized codes

**Option B: Migrate Existing Data**
1. Export current inventory to CSV
2. Map existing codes to catalog codes
3. Re-import with catalog codes
4. Validate no duplicates

---

## 🎯 Benefits Summary

### For Station Managers
- ✅ Can't accidentally create duplicate/conflicting codes
- ✅ Browse professional catalog with specs
- ✅ Fast setup (select from pre-defined list)
- ✅ Easy to demo different station types

### For System Administrators
- ✅ Central control over item definitions
- ✅ Consistent data across all stations
- ✅ Easy to add new standardized items
- ✅ Quality assurance (all items have proper specs)

### For Multi-Station Future
- ✅ When adding multi-station sync later, all stations speak same language
- ✅ "Request GAUZE-4X4 from LOG-01" is unambiguous
- ✅ Inventory reports aggregated correctly

---

## 🚀 Next Steps

**Immediate (This Week):**
1. Review master catalog - add any missing items?
2. Decide: Full implementation or just use for new deployments?
3. Test catalog loading in fresh database

**Phase 1 Implementation (Next Sprint):**
1. Backend: Disable custom code creation
2. Backend: Add catalog search APIs
3. Update all 4 station profiles to SELECT from catalog
4. Test fresh deployment with each profile

**Phase 2 Implementation (Sprint After):**
1. Build catalog browser UI
2. Replace "新增物品" with "從目錄新增"
3. User testing with station managers

---

## 📝 Open Questions

1. **Should we allow station-specific custom items?**
   - Current plan: No, all items must be in catalog
   - Alternative: Allow but mark as "非標準品項"

2. **Who maintains the master catalog?**
   - Proposal: Medical director + IT admin
   - Updates pushed via system updates

3. **How to handle rare/specialty items?**
   - Request addition to catalog
   - Admin reviews and approves
   - Added in next catalog version

---

## 📦 Current Master Catalog Contents

- **Consumables**: 50+ items
  - Protective equipment (gloves, masks, gowns)
  - Gauze & bandages
  - Syringes & needles (all sizes)
  - IV supplies
  - Disinfection supplies

- **Medicines**: 20+ items
  - Pain relief (paracetamol, ibuprofen, morphine)
  - Antibiotics (amoxicillin, cephalexin)
  - Emergency drugs (epinephrine, atropine)
  - IV fluids (saline, dextrose, LR)

- **Equipment**: 30+ items
  - Power & environmental (generators, purifiers)
  - Surgical instruments (BORP-specific)
  - Diagnostic tools (BP monitor, oximeter)

**Total**: 100+ standardized items

---

## ✅ Approval Checklist

- [ ] Medical director reviews item list
- [ ] IT approves technical architecture
- [ ] Station managers test catalog browser
- [ ] Security review (who can add catalog items?)
- [ ] Training materials prepared
- [ ] Migration plan tested

---

*Last Updated: 2025-11-23*
*Version: 1.0.0*
*Status: Awaiting approval for Phase 1 implementation*
