"""
MIRS 全域唯一站點識別系統
Station Identity Management System

生成格式: {TYPE}-{TIMESTAMP}-{UUID}
範例: HC-250130-a3f2

站點類型代碼:
- HC: Health Center (衛生所/基層醫療站)
- SURG: Surgical Station (手術站)
- LOGI: Logistics Hub (後勤中樞)
- HOSP: Hospital (醫院/自訂醫療機構)
"""

import uuid
from datetime import datetime
from typing import Dict, Optional


class StationIdentity:
    """全域唯一站點識別系統"""

    # 站點類型映射
    STATION_TYPES = {
        'health_center': {
            'prefix': 'HC',
            'name': '衛生所',
            'name_en': 'Health Center',
            'category': 'HEALTH_CENTER'
        },
        'surgical_station': {
            'prefix': 'BORP',
            'name': '備援手術室',
            'name_en': 'Backup Operating Room Point',
            'category': 'SURGICAL_STATION'
        },
        'logistics_hub': {
            'prefix': 'LOG',
            'name': '物資中心',
            'name_en': 'Logistics Hub',
            'category': 'LOGISTICS_HUB'
        },
        'hospital_custom': {
            'prefix': 'HOSP',
            'name': '醫院站',
            'name_en': 'Hospital Custom',
            'category': 'HOSPITAL'
        }
    }

    # 反向映射：prefix -> profile
    PREFIX_TO_PROFILE = {
        'HC': 'health_center',
        'BORP': 'surgical_station',
        'LOG': 'logistics_hub',
        'HOSP': 'hospital_custom'
    }

    @staticmethod
    def generate_station_id(
        station_type: str,
        org_code: str,
        timestamp: Optional[str] = None,
        unique_id: Optional[str] = None
    ) -> str:
        """
        生成全域唯一站點ID（混合格式 v2.0）

        Args:
            station_type: Profile名稱 (health_center, surgical_station, logistics_hub, hospital_custom)
            org_code: 組織代碼（必填，例如: VGH, CMUH, DNO）
            timestamp: 選填，時間戳 YYMMDD（預設為當前日期）
            unique_id: 選填，唯一識別碼（預設為隨機UUID4前4碼）

        Returns:
            格式化的站點ID: TYPE-ORG-YYMMDD-UUID

        Examples:
            >>> StationIdentity.generate_station_id('surgical_station', 'VGH')
            'BORP-VGH-250201-a3f2'

            >>> StationIdentity.generate_station_id('health_center', 'CMUH')
            'HC-CMUH-250201-b8f1'
        """
        if station_type not in StationIdentity.STATION_TYPES:
            raise ValueError(f"Invalid station type: {station_type}")

        if not org_code:
            raise ValueError("org_code is required")

        # 取得站點類型前綴
        prefix = StationIdentity.STATION_TYPES[station_type]['prefix']

        # 生成時間戳（年月日格式：YYMMDD）
        if timestamp is None:
            timestamp = datetime.now().strftime("%y%m%d")

        # 生成唯一識別碼（UUID4 前4碼）
        if unique_id is None:
            unique_id = str(uuid.uuid4())[:4]

        # 組合站點ID: TYPE-ORG-YYMMDD-UUID
        return f"{prefix}-{org_code}-{timestamp}-{unique_id}"

    @staticmethod
    def parse_station_id(station_id: str) -> Dict[str, str]:
        """
        解析站點ID（支援混合格式 v2.0）

        Args:
            station_id: 站點ID字串

        Returns:
            包含解析結果的字典

        Examples:
            >>> StationIdentity.parse_station_id('BORP-VGH-250201-a3f2')
            {'prefix': 'BORP', 'org': 'VGH', 'timestamp': '250201', 'uuid': 'a3f2', 'profile': 'surgical_station'}

            >>> StationIdentity.parse_station_id('HC-CMUH-250202-b8f1')
            {'prefix': 'HC', 'org': 'CMUH', 'timestamp': '250202', 'uuid': 'b8f1', 'profile': 'health_center'}
        """
        parts = station_id.split('-')

        if len(parts) == 4:
            # 混合格式 v2.0: TYPE-ORG-YYMMDD-UUID
            return {
                'prefix': parts[0],
                'org': parts[1],
                'timestamp': parts[2],
                'uuid': parts[3],
                'profile': StationIdentity.PREFIX_TO_PROFILE.get(parts[0], 'unknown')
            }
        elif len(parts) == 3:
            # 舊格式 (向後相容): TYPE-NUMBER
            # 例如: BORP-VGH-01
            return {
                'prefix': parts[0],
                'org': parts[1],
                'number': parts[2],
                'timestamp': None,
                'uuid': None,
                'profile': StationIdentity.PREFIX_TO_PROFILE.get(parts[0], 'unknown')
            }
        else:
            raise ValueError(f"Invalid station ID format: {station_id}")

    @staticmethod
    def get_station_type_info(profile: str) -> Dict[str, str]:
        """
        取得站點類型資訊

        Args:
            profile: Profile名稱

        Returns:
            站點類型資訊字典
        """
        return StationIdentity.STATION_TYPES.get(profile, {})

    @staticmethod
    def validate_station_id(station_id: str) -> bool:
        """
        驗證站點ID格式是否正確

        Args:
            station_id: 站點ID字串

        Returns:
            True if valid, False otherwise
        """
        try:
            parsed = StationIdentity.parse_station_id(station_id)
            return parsed['prefix'] in StationIdentity.PREFIX_TO_PROFILE
        except (ValueError, KeyError, IndexError):
            return False

    @staticmethod
    def generate_display_name(station_id: str, custom_name: Optional[str] = None) -> str:
        """
        生成站點顯示名稱

        Args:
            station_id: 站點ID
            custom_name: 自訂名稱（選填）

        Returns:
            格式化的顯示名稱

        Examples:
            >>> StationIdentity.generate_display_name('HC-250130-a3f2')
            'HC-250130-a3f2 衛生所'

            >>> StationIdentity.generate_display_name('HC-250130-a3f2', '臺北衛生所')
            'HC-250130-a3f2 臺北衛生所'
        """
        try:
            parsed = StationIdentity.parse_station_id(station_id)
            profile = parsed['profile']
            type_info = StationIdentity.STATION_TYPES.get(profile, {})

            if custom_name:
                return f"{station_id} {custom_name}"
            else:
                default_name = type_info.get('name', '醫療站')
                return f"{station_id} {default_name}"
        except ValueError:
            return station_id


# 使用範例
if __name__ == "__main__":
    print("=== MIRS v2.0 混合格式 ID 生成器測試 ===\n")

    # 測試組織代碼
    test_orgs = ['VGH', 'CMUH', 'DNO']

    # 生成不同類型的站點ID
    print("【測試 1】生成不同類型站點ID:")
    for profile in StationIdentity.STATION_TYPES.keys():
        org = test_orgs[list(StationIdentity.STATION_TYPES.keys()).index(profile) % len(test_orgs)]
        station_id = StationIdentity.generate_station_id(profile, org)
        print(f"  {profile:20} → {station_id}")

    print("\n【測試 2】解析混合格式站點ID:")
    test_ids = [
        'BORP-VGH-250201-a3f2',
        'HC-CMUH-250202-b8f1',
        'LOG-DNO-250203-c9e2',
        'BORP-VGH-01'  # 舊格式 (向後相容)
    ]
    for test_id in test_ids:
        try:
            parsed = StationIdentity.parse_station_id(test_id)
            print(f"  {test_id:25} → Type: {parsed['prefix']}, Org: {parsed['org']}, Profile: {parsed['profile']}")
        except ValueError as e:
            print(f"  {test_id:25} → ✗ {e}")

    print("\n【測試 3】驗證站點ID格式:")
    validate_ids = [
        ('BORP-VGH-250201-a3f2', True),
        ('HC-CMUH-250202-b8f1', True),
        ('BORP-VGH-01', True),  # 舊格式
        ('INVALID-ID', False)
    ]
    for test_id, expected in validate_ids:
        result = StationIdentity.validate_station_id(test_id)
        status = '✓' if result == expected else '✗'
        print(f"  {status} {test_id:25} → {result}")

    print("\n【測試 4】生成顯示名稱:")
    display_ids = [
        ('BORP-VGH-250201-a3f2', None),
        ('BORP-VGH-250201-a3f2', '榮總備援手術室 01'),
        ('HC-CMUH-250202-b8f1', '中國醫衛生所')
    ]
    for test_id, custom_name in display_ids:
        display = StationIdentity.generate_display_name(test_id, custom_name)
        print(f"  {display}")

    print("\n" + "=" * 60)
    print("測試完成！")
