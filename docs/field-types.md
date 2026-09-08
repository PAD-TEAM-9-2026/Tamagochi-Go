# Field types

Every request and response shape used by the eight services, grouped by the
service that uses it, then alphabetically. Referenced from the contract section
of the [README](../README.md).

These are JSON shapes sent over HTTP and RabbitMQ, not database tables. A shape
in the first section is one that appears in more than one service's API, so both
sides agree on the JSON. Each service still stores its own data in its own
database.

## Used by more than one service

### ActorInput

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |

### Empty

| Field | Type / constraint | Required |
|---|---|---|

### Health

| Field | Type / constraint | Required |
|---|---|---|
| `status` | UP | yes |

### Problem

| Field | Type / constraint | Required |
|---|---|---|
| `type` | "about:blank" | yes |
| `title` | string [1..128] | yes |
| `status` | integer [400..599] | yes |
| `detail` | string [1..1024] | yes |
| `instance` | string [1..2048] | yes |
| `code` | string [1..64] | yes |
| `correlation_id` | uuid (v7) | yes |

### Readiness

| Field | Type / constraint | Required |
|---|---|---|
| `status` | READY / NOT_READY | yes |

### VersionReceipt

| Field | Type / constraint | Required |
|---|---|---|
| `version` | integer [1..2147483647] | yes |

## User Management

### BattleSettlement

| Field | Type / constraint | Required |
|---|---|---|
| `battle_id` | uuid (v7) | yes |
| `winner_id` | uuid (v7) | yes |
| `loser_id` | uuid (v7) | yes |
| `winner_credit` | 50 | yes |
| `loser_debit` | integer [0..20] | yes |
| `winner_balance` | integer [0..9007199254740991] | yes |
| `loser_balance` | integer [0..9007199254740991] | yes |

### BattleSettlementInput

| Field | Type / constraint | Required |
|---|---|---|
| `battle_id` | uuid (v7) | yes |
| `winner_id` | uuid (v7) | yes |
| `loser_id` | uuid (v7) | yes |

### Boost

| Field | Type / constraint | Required |
|---|---|---|
| `boost_id` | ATTACK_10 | yes |
| `charges` | integer [0..100] | yes |
| `attack_bps` | 1000 | yes |

### BoostPage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<Boost> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### BoostReceipt

| Field | Type / constraint | Required |
|---|---|---|
| `battle_id` | uuid (v7) | yes |
| `user_id` | uuid (v7) | yes |
| `boost_id` | ATTACK_10 | yes |
| `attack_bps` | 1000 | yes |
| `remaining_charges` | integer [0..100] | yes |

### ConsumeBoost

| Field | Type / constraint | Required |
|---|---|---|
| `battle_id` | uuid (v7) | yes |
| `user_id` | uuid (v7) | yes |
| `boost_id` | ATTACK_10 | yes |

### Credit

| Field | Type / constraint | Required |
|---|---|---|
| `amount` | integer [0..1000000] | yes |
| `reason` | RAID_WIN | yes |
| `reference_id` | uuid (v7) | yes |

### CreditReceipt

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `credited_amount` | integer [0..9007199254740991] | yes |
| `new_balance` | integer [0..9007199254740991] | yes |
| `reference_id` | uuid (v7) | yes |

### FriendRequest

| Field | Type / constraint | Required |
|---|---|---|
| `request_id` | uuid (v7) | yes |
| `from_user_id` | uuid (v7) | yes |
| `to_user_id` | uuid (v7) | yes |
| `status` | PENDING / ACCEPTED / REJECTED / EXPIRED / CANCELLED | yes |
| `expires_at` | timestamp (ISO 8601 UTC) | yes |

### FriendRequestInput

| Field | Type / constraint | Required |
|---|---|---|
| `to_user_id` | uuid (v7) | yes |

### FriendRequestPage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<FriendRequest> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### JoinPackage

| Field | Type / constraint | Required |
|---|---|---|
| `package_id` | uuid (v7) | yes |

### Jwk

| Field | Type / constraint | Required |
|---|---|---|
| `kty` | "RSA" | yes |
| `use` | "sig" | yes |
| `alg` | "RS256" | yes |
| `kid` | string [1..128] | yes |
| `n` | string [1..2048] | yes |
| `e` | string [1..32] | yes |

### Jwks

| Field | Type / constraint | Required |
|---|---|---|
| `keys` | array<Jwk> [1..5] | yes |

### LocalCredit

| Field | Type / constraint | Required |
|---|---|---|
| `package_id` | uuid (v7) | yes |
| `config_version` | integer [1..2147483647] | yes |
| `action` | string [1..64] | yes |
| `care_action_id` | uuid (v7) | yes |

### Login

| Field | Type / constraint | Required |
|---|---|---|
| `email` | email | yes |
| `password` | string [1..128] | yes |
| `package_id` | uuid (v7) | yes |

### MembershipPage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<MembershipSnapshot> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### MembershipSnapshot

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `package_ids` | array<uuid (v7)> [1..20] | yes |
| `membership_version` | integer [1..2147483647] | yes |

### Refresh

| Field | Type / constraint | Required |
|---|---|---|
| `refresh_token` | string [1..512] | yes |

### Register

| Field | Type / constraint | Required |
|---|---|---|
| `username` | string [3..32] | yes |
| `email` | email | yes |
| `password` | string [12..128] | yes |
| `package_id` | uuid (v7) | yes |

### Registration

| Field | Type / constraint | Required |
|---|---|---|
| `user` | User | yes |
| `global_currency` | integer [0..9007199254740991] | yes |
| `starter_status` | PENDING | yes |

### RejoinStatus

| Field | Type / constraint | Required |
|---|---|---|
| `package_id` | uuid (v7) | yes |
| `can_rejoin` | boolean | yes |
| `cooldown_expires_at` | timestamp (ISO 8601 UTC) or null | yes |

### Relationship

| Field | Type / constraint | Required |
|---|---|---|
| `relationship` | friend / enemy / stranger | yes |
| `reverse_relationship` | friend / enemy / stranger | yes |
| `version` | integer [1..2147483647] | yes |

### RelationshipItem

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `relationship` | friend / enemy | yes |

### RelationshipPage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<RelationshipItem> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### ServiceToken

| Field | Type / constraint | Required |
|---|---|---|
| `access_token` | string [1..8192] | yes |
| `token_type` | Bearer | yes |
| `expires_in` | 300 | yes |

### ServiceTokenRequest

| Field | Type / constraint | Required |
|---|---|---|
| `audience` | user-management / tamagotchi / battle / guild / package-registry / map / monster-raid / notification | yes |
| `scopes` | array<string [1..64]> [0..20] | yes |

### Tokens

| Field | Type / constraint | Required |
|---|---|---|
| `access_token` | string [1..8192] | yes |
| `refresh_token` | string [1..512] | yes |
| `token_type` | Bearer | yes |
| `expires_in` | 900 | yes |

### User

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `username` | string [3..32] | yes |
| `email` | email | yes |
| `package_ids` | array<uuid (v7)> [1..20] | yes |
| `membership_version` | integer [1..2147483647] | yes |

### UserFriendRequestCreatedEvent

| Field | Type / constraint | Required |
|---|---|---|
| `event_id` | uuid (v7) | yes |
| `event_type` | "user.friend_request_created.v1" | yes |
| `occurred_at` | timestamp (ISO 8601 UTC) | yes |
| `producer` | "user-management" | yes |
| `correlation_id` | uuid (v7) | yes |
| `data` | object {request_id: uuid (v7), from_user_id: uuid (v7), to_user_id: uuid (v7), expires_at: date-time} | yes |

### UserPackageJoinedEvent

| Field | Type / constraint | Required |
|---|---|---|
| `event_id` | uuid (v7) | yes |
| `event_type` | "user.package_joined.v1" | yes |
| `occurred_at` | timestamp (ISO 8601 UTC) | yes |
| `producer` | "user-management" | yes |
| `correlation_id` | uuid (v7) | yes |
| `data` | object {user_id: uuid (v7), package_ids: array<uuid (v7)> [1..20], membership_version: integer [1..2147483647]} | yes |

### UserProfile

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `username` | string [3..32] | yes |

### Wallet

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `package_id` | uuid (v7) or null | yes |
| `amount` | integer [0..9007199254740991] | yes |

## Tamagotchi

### CareInput

| Field | Type / constraint | Required |
|---|---|---|
| `action` | string [1..64] | yes |

### CareReceipt

| Field | Type / constraint | Required |
|---|---|---|
| `care_action_id` | uuid (v7) | yes |
| `tamagotchi` | Tamagotchi | yes |
| `currency_status` | PENDING | yes |

### Collection

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `primary` | Tamagotchi or null | yes |
| `secondary` | array<Tamagotchi> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |
| `retrieved_at` | timestamp (ISO 8601 UTC) | yes |

### Engagement

| Field | Type / constraint | Required |
|---|---|---|
| `engagement_id` | uuid (v7) | yes |
| `battle_id` | uuid (v7) | yes |
| `status` | ACTIVE / RELEASED | yes |
| `pets` | array<Tamagotchi> [4..4] | yes |
| `created_at` | timestamp (ISO 8601 UTC) | yes |

### EngagementInput

| Field | Type / constraint | Required |
|---|---|---|
| `battle_id` | uuid (v7) | yes |
| `lineups` | array<Lineup> [2..2] | yes |

### Lineup

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `primary_id` | uuid (v7) | yes |
| `secondary_id` | uuid (v7) | yes |

### Mint

| Field | Type / constraint | Required |
|---|---|---|
| `owner_user_id` | uuid (v7) | yes |
| `package_id` | uuid (v7) | yes |

### PrimaryInput

| Field | Type / constraint | Required |
|---|---|---|
| `tamagotchi_id` | uuid (v7) | yes |

### PrimarySelection

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `tamagotchi_id` | uuid (v7) or null | yes |
| `version` | integer [1..2147483647] | yes |

### Tamagotchi

| Field | Type / constraint | Required |
|---|---|---|
| `id` | uuid (v7) | yes |
| `name` | string [1..64] | yes |
| `origin_package_id` | uuid (v7) | yes |
| `config_version` | integer [1..2147483647] | yes |
| `owner_user_id` | uuid (v7) | yes |
| `role` | PRIMARY / SECONDARY | yes |
| `combat_type` | FLAME / NATURE / EARTH / ELECTRIC / WATER / SHADOW | yes |
| `level` | integer [1..100] | yes |
| `xp` | integer [0..9007199254740991] | yes |
| `sprite_ref` | string [1..512] | yes |
| `package_stats` | map<string, ['number', 'string', 'boolean']> (bounded by schema) | yes |
| `acquired_at` | timestamp (ISO 8601 UTC) | yes |
| `version` | integer [1..2147483647] | yes |

### TamagotchiCreatedEvent

| Field | Type / constraint | Required |
|---|---|---|
| `event_id` | uuid (v7) | yes |
| `event_type` | "tamagotchi.created.v1" | yes |
| `occurred_at` | timestamp (ISO 8601 UTC) | yes |
| `producer` | "tamagotchi" | yes |
| `correlation_id` | uuid (v7) | yes |
| `data` | object {tamagotchi_id: uuid (v7), owner_user_id: uuid (v7), origin_package_id: uuid (v7)} | yes |

### TamagotchiLeveledUpEvent

| Field | Type / constraint | Required |
|---|---|---|
| `event_id` | uuid (v7) | yes |
| `event_type` | "tamagotchi.leveled_up.v1" | yes |
| `occurred_at` | timestamp (ISO 8601 UTC) | yes |
| `producer` | "tamagotchi" | yes |
| `correlation_id` | uuid (v7) | yes |
| `data` | object {tamagotchi_id: uuid (v7), owner_user_id: uuid (v7), level: integer [2..100], source_id: uuid (v7)} | yes |

### TamagotchiOwnershipTransferredEvent

| Field | Type / constraint | Required |
|---|---|---|
| `event_id` | uuid (v7) | yes |
| `event_type` | "tamagotchi.ownership_transferred.v1" | yes |
| `occurred_at` | timestamp (ISO 8601 UTC) | yes |
| `producer` | "tamagotchi" | yes |
| `correlation_id` | uuid (v7) | yes |
| `data` | object {tamagotchi_id: uuid (v7), tamagotchi_name: string [1..64], combat_type: FLAME / NATURE / EARTH / ELECTRIC / WATER / SHADOW, level: integer [1..100], previous_owner_user_id: uuid (v7), new_owner_user_id: uuid (v7), reason: "BATTLE_LOSS", battle_id: uuid (v7)} | yes |

### TamagotchiPage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<Tamagotchi> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### TransferInput

| Field | Type / constraint | Required |
|---|---|---|
| `from_user_id` | uuid (v7) | yes |
| `to_user_id` | uuid (v7) | yes |
| `reason` | BATTLE_LOSS | yes |
| `reference_id` | uuid (v7) | yes |
| `engagement_id` | uuid (v7) | yes |

### TransferReceipt

| Field | Type / constraint | Required |
|---|---|---|
| `id` | uuid (v7) | yes |
| `previous_owner_user_id` | uuid (v7) | yes |
| `owner_user_id` | uuid (v7) | yes |
| `role` | "SECONDARY" | yes |
| `version` | integer [1..2147483647] | yes |
| `transferred_at` | timestamp (ISO 8601 UTC) | yes |

### TypeList

| Field | Type / constraint | Required |
|---|---|---|
| `types` | array<FLAME / NATURE / EARTH / ELECTRIC / WATER / SHADOW> [0..6] | yes |
| `version` | integer [1..2147483647] | yes |

### TypeMatrix

| Field | Type / constraint | Required |
|---|---|---|
| `types` | array<FLAME / NATURE / EARTH / ELECTRIC / WATER / SHADOW> [0..6] | yes |
| `version` | integer [1..2147483647] | yes |
| `matrix` | object {FLAME: object {FLAME: 7500 / 10000 / 15000, NATURE: 7500 / 10000 / 15000, EARTH: 7500 / 10000 / 15000, ELECTRIC: 7500 / 10000 / 15000, WATER: 7500 / 10000 / 15000, SHADOW: 7500 / 10000 / 15000}, NATURE: object {FLAME: 7500 / 10000 / 15000, NATURE: 7500 / 10000 / 15000, EARTH: 7500 / 10000 / 15000, ELECTRIC: 7500 / 10000 / 15000, WATER: 7500 / 10000 / 15000, SHADOW: 7500 / 10000 / 15000}, EARTH: object {FLAME: 7500 / 10000 / 15000, NATURE: 7500 / 10000 / 15000, EARTH: 7500 / 10000 / 15000, ELECTRIC: 7500 / 10000 / 15000, WATER: 7500 / 10000 / 15000, SHADOW: 7500 / 10000 / 15000}, ELECTRIC: object {FLAME: 7500 / 10000 / 15000, NATURE: 7500 / 10000 / 15000, EARTH: 7500 / 10000 / 15000, ELECTRIC: 7500 / 10000 / 15000, WATER: 7500 / 10000 / 15000, SHADOW: 7500 / 10000 / 15000}, WATER: object {FLAME: 7500 / 10000 / 15000, NATURE: 7500 / 10000 / 15000, EARTH: 7500 / 10000 / 15000, ELECTRIC: 7500 / 10000 / 15000, WATER: 7500 / 10000 / 15000, SHADOW: 7500 / 10000 / 15000}, SHADOW: object {FLAME: 7500 / 10000 / 15000, NATURE: 7500 / 10000 / 15000, EARTH: 7500 / 10000 / 15000, ELECTRIC: 7500 / 10000 / 15000, WATER: 7500 / 10000 / 15000, SHADOW: 7500 / 10000 / 15000}} | yes |

### XpInput

| Field | Type / constraint | Required |
|---|---|---|
| `amount` | integer [0..1000000] | yes |
| `source` | BATTLE / RAID | yes |
| `source_id` | uuid (v7) | yes |

### XpReceipt

| Field | Type / constraint | Required |
|---|---|---|
| `id` | uuid (v7) | yes |
| `xp` | integer [0..9007199254740991] | yes |
| `level` | integer [1..100] | yes |
| `levels_gained` | integer [0..99] | yes |
| `version` | integer [1..2147483647] | yes |

## Battle

### Battle

| Field | Type / constraint | Required |
|---|---|---|
| `battle_id` | uuid (v7) | yes |
| `challenger_id` | uuid (v7) | yes |
| `opponent_id` | uuid (v7) | yes |
| `status` | PENDING_ACCEPT / PREPARING / ONGOING / COMPLETED / REJECTED / EXPIRED / CANCELLED | yes |
| `sides` | array<BattleSide> [0..2] | yes |
| `turn_user_id` | uuid (v7) or null | yes |
| `turn_expires_at` | date-time or null | yes |
| `expires_at` | timestamp (ISO 8601 UTC) | yes |
| `winner_id` | uuid (v7) or null | yes |
| `loser_id` | uuid (v7) or null | yes |
| `settlement_status` | NOT_READY / PENDING / PARTIAL / DELIVERED / NOT_APPLICABLE / NEEDS_ATTENTION | yes |
| `version` | integer [1..2147483647] | yes |

### BattleAccept

| Field | Type / constraint | Required |
|---|---|---|
| `primary_id` | uuid (v7) | yes |
| `secondary_id` | uuid (v7) | yes |
| `boost_ids` | array<ATTACK_10> [0..1] | yes |

### BattleAttack

| Field | Type / constraint | Required |
|---|---|---|
| `battle_id` | uuid (v7) | yes |
| `attacker_id` | uuid (v7) | yes |
| `damage_dealt` | integer [1..1500] | yes |
| `opponent_hp_remaining` | integer [0..1500] | yes |
| `next_turn` | uuid (v7) or null | yes |
| `status` | ONGOING / COMPLETED | yes |
| `version` | integer [1..2147483647] | yes |

### BattleCompletedEvent

| Field | Type / constraint | Required |
|---|---|---|
| `event_id` | uuid (v7) | yes |
| `event_type` | "battle.completed.v1" | yes |
| `occurred_at` | timestamp (ISO 8601 UTC) | yes |
| `producer` | "battle" | yes |
| `correlation_id` | uuid (v7) | yes |
| `data` | object {battle_id: uuid (v7), winner_id: uuid (v7), loser_id: uuid (v7), settlement_status: "PENDING"} | yes |

### BattleInput

| Field | Type / constraint | Required |
|---|---|---|
| `opponent_id` | uuid (v7) | yes |
| `primary_id` | uuid (v7) | yes |
| `secondary_id` | uuid (v7) | yes |
| `boost_ids` | array<ATTACK_10> [0..1] | yes |

### BattlePage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<Battle> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### BattleRequestCreatedEvent

| Field | Type / constraint | Required |
|---|---|---|
| `event_id` | uuid (v7) | yes |
| `event_type` | "battle.request_created.v1" | yes |
| `occurred_at` | timestamp (ISO 8601 UTC) | yes |
| `producer` | "battle" | yes |
| `correlation_id` | uuid (v7) | yes |
| `data` | object {battle_id: uuid (v7), challenger_id: uuid (v7), opponent_id: uuid (v7), expires_at: date-time} | yes |

### BattleSide

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `primary_id` | uuid (v7) | yes |
| `secondary_id` | uuid (v7) | yes |
| `current_hp` | integer [0..1500] | yes |
| `max_hp` | integer [1..1500] | yes |

## Guild

### ChatMessage

| Field | Type / constraint | Required |
|---|---|---|
| `message_id` | uuid (v7) | yes |
| `guild_id` | uuid (v7) | yes |
| `author_id` | uuid (v7) | yes |
| `client_message_id` | uuid (v7) | yes |
| `content` | string [1..2000] | yes |
| `timestamp` | timestamp (ISO 8601 UTC) | yes |

### ChatPage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<ChatMessage> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### Guild

| Field | Type / constraint | Required |
|---|---|---|
| `guild_id` | uuid (v7) | yes |
| `name` | string [3..64] | yes |
| `description` | string [0..500] | yes |
| `leader_id` | uuid (v7) | yes |
| `member_count` | integer [1..100] | yes |
| `version` | integer [1..2147483647] | yes |

### GuildInput

| Field | Type / constraint | Required |
|---|---|---|
| `name` | string [3..64] | yes |
| `description` | string [0..500] | yes |

### GuildInvitationCreatedEvent

| Field | Type / constraint | Required |
|---|---|---|
| `event_id` | uuid (v7) | yes |
| `event_type` | "guild.invitation_created.v1" | yes |
| `occurred_at` | timestamp (ISO 8601 UTC) | yes |
| `producer` | "guild" | yes |
| `correlation_id` | uuid (v7) | yes |
| `data` | object {invitation_id: uuid (v7), guild_id: uuid (v7), guild_name: string [1..64], invited_user_id: uuid (v7), invited_by_user_id: uuid (v7), expires_at: date-time} | yes |

### GuildMemberJoinedEvent

| Field | Type / constraint | Required |
|---|---|---|
| `event_id` | uuid (v7) | yes |
| `event_type` | "guild.member_joined.v1" | yes |
| `occurred_at` | timestamp (ISO 8601 UTC) | yes |
| `producer` | "guild" | yes |
| `correlation_id` | uuid (v7) | yes |
| `data` | object {guild_id: uuid (v7), user_id: uuid (v7), membership_version: integer [1..2147483647]} | yes |

### GuildMemberLeftEvent

| Field | Type / constraint | Required |
|---|---|---|
| `event_id` | uuid (v7) | yes |
| `event_type` | "guild.member_left.v1" | yes |
| `occurred_at` | timestamp (ISO 8601 UTC) | yes |
| `producer` | "guild" | yes |
| `correlation_id` | uuid (v7) | yes |
| `data` | object {guild_id: uuid (v7), user_id: uuid (v7), membership_version: integer [1..2147483647]} | yes |

### GuildPage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<Guild> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### Invitation

| Field | Type / constraint | Required |
|---|---|---|
| `invitation_id` | uuid (v7) | yes |
| `guild_id` | uuid (v7) | yes |
| `invited_user_id` | uuid (v7) | yes |
| `invited_by_user_id` | uuid (v7) | yes |
| `status` | PENDING / ACCEPTED / DECLINED / REVOKED / EXPIRED | yes |
| `expires_at` | timestamp (ISO 8601 UTC) | yes |

### InvitationInput

| Field | Type / constraint | Required |
|---|---|---|
| `invited_user_id` | uuid (v7) | yes |

### InvitationPage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<Invitation> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### LeaderInput

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |

### Member

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `role` | LEADER / OFFICER / MEMBER | yes |

### Members

| Field | Type / constraint | Required |
|---|---|---|
| `guild_id` | uuid (v7) | yes |
| `members` | array<Member> [1..100] | yes |
| `version` | integer [1..2147483647] | yes |
| `retrieved_at` | timestamp (ISO 8601 UTC) | yes |

### RoleInput

| Field | Type / constraint | Required |
|---|---|---|
| `role` | OFFICER / MEMBER | yes |
| `expected_guild_version` | integer [1..2147483647] | yes |

### WsAck

| Field | Type / constraint | Required |
|---|---|---|
| `type` | "ack" | yes |
| `client_message_id` | uuid (v7) | yes |
| `message_id` | uuid (v7) | yes |
| `timestamp` | timestamp (ISO 8601 UTC) | yes |

### WsAuth

| Field | Type / constraint | Required |
|---|---|---|
| `type` | "auth" | yes |
| `access_token` | string [1..8192] | yes |

### WsError

| Field | Type / constraint | Required |
|---|---|---|
| `type` | "error" | yes |
| `code` | string [1..64] | yes |
| `detail` | string [1..256] | yes |
| `client_message_id` | uuid (v7) | no |

### WsMessage

| Field | Type / constraint | Required |
|---|---|---|
| `type` | "message" | yes |
| `message` | ChatMessage | yes |

### WsReady

| Field | Type / constraint | Required |
|---|---|---|
| `type` | "ready" | yes |
| `guild_id` | uuid (v7) | yes |
| `user_id` | uuid (v7) | yes |
| `expires_at` | timestamp (ISO 8601 UTC) | yes |

### WsSend

| Field | Type / constraint | Required |
|---|---|---|
| `type` | "send" | yes |
| `client_message_id` | uuid (v7) | yes |
| `content` | string [1..2000] | yes |

## Package Registry

### Asset

| Field | Type / constraint | Required |
|---|---|---|
| `sprite_ref` | string [1..512] | yes |
| `url` | uri | yes |

### Assets

| Field | Type / constraint | Required |
|---|---|---|
| `package_id` | uuid (v7) | yes |
| `config_version` | integer [1..2147483647] | yes |
| `items` | array<Asset> [1..100] | yes |

### Bonuses

| Field | Type / constraint | Required |
|---|---|---|
| `package_id` | uuid (v7) | yes |
| `config_version` | integer [1..2147483647] | yes |
| `bonuses` | array<BonusRule> [0..32] | yes |

### BonusRule

| Field | Type / constraint | Required |
|---|---|---|
| `stat_key` | string [1..64] | yes |
| `operator` | GT / GTE / LT / LTE | yes |
| `threshold` | number [-1000000..1000000] | yes |
| `effect` | ATTACK_BPS / DEFENSE_BPS | yes |
| `value_bps` | integer [0..5000] | yes |

### Boss

| Field | Type / constraint | Required |
|---|---|---|
| `boss_id` | uuid (v7) | yes |
| `config_version` | integer [1..2147483647] | yes |
| `definition` | BossInput | yes |

### BossInput

| Field | Type / constraint | Required |
|---|---|---|
| `name` | string [1..64] | yes |
| `description` | string [0..1000] | yes |
| `sprite_ref` | string [1..512] | yes |
| `combat_type` | FLAME / NATURE / EARTH / ELECTRIC / WATER / SHADOW | yes |
| `max_hp` | integer [1..1000000000] | yes |
| `defense` | integer [0..1000000] | yes |
| `weaknesses` | array<FLAME / NATURE / EARTH / ELECTRIC / WATER / SHADOW> [0..6] | yes |
| `resistances` | array<FLAME / NATURE / EARTH / ELECTRIC / WATER / SHADOW> [0..6] | yes |
| `special_properties` | Empty | yes |
| `duration_seconds` | integer [1..3600] | yes |
| `max_participants` | integer [1..100] | yes |
| `rewards` | object {global_currency: integer [0..1000000], xp: integer [0..1000000]} | yes |

### BossPage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<Boss> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### CareDelta

| Field | Type / constraint | Required |
|---|---|---|
| `stat_key` | string [1..64] | yes |
| `delta` | number [-1000000..1000000] | yes |

### CareRule

| Field | Type / constraint | Required |
|---|---|---|
| `action` | string [1..64] | yes |
| `deltas` | array<CareDelta> [0..32] | yes |
| `xp` | integer [0..1000] | yes |
| `cooldown_seconds` | integer [1..86400] | yes |
| `local_currency` | integer [0..10000] | yes |

### CurrencyRules

| Field | Type / constraint | Required |
|---|---|---|
| `package_id` | uuid (v7) | yes |
| `config_version` | integer [1..2147483647] | yes |
| `daily_currency_cap` | integer [0..1000000] | yes |
| `care_actions` | array<CareRule> [1..32] | yes |

### Eligibility

| Field | Type / constraint | Required |
|---|---|---|
| `eligible` | boolean | yes |
| `eligible_package_ids` | array<uuid (v7)> [0..20] | yes |
| `reason` | string [1..256] or null | yes |

### EligibilityInput

| Field | Type / constraint | Required |
|---|---|---|
| `user_packages` | array<uuid (v7)> [1..20] | yes |

### Occurrence

| Field | Type / constraint | Required |
|---|---|---|
| `occurrence_id` | uuid (v7) | yes |
| `boss_id` | uuid (v7) | yes |
| `boss_version` | integer [1..2147483647] | yes |
| `available_from` | timestamp (ISO 8601 UTC) | yes |
| `available_until` | timestamp (ISO 8601 UTC) | yes |
| `status` | scheduled / active / inactive / cancelled | yes |
| `version` | integer [1..2147483647] | yes |

### OccurrenceInput

| Field | Type / constraint | Required |
|---|---|---|
| `boss_id` | uuid (v7) | yes |
| `boss_version` | integer [1..2147483647] | yes |
| `available_from` | timestamp (ISO 8601 UTC) | yes |
| `available_until` | timestamp (ISO 8601 UTC) | yes |

### OccurrencePage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<Occurrence> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### OccurrenceReceipt

| Field | Type / constraint | Required |
|---|---|---|
| `occurrence` | Occurrence | yes |
| `runtime_propagation` | PENDING | yes |

### Package

| Field | Type / constraint | Required |
|---|---|---|
| `package_id` | uuid (v7) | yes |
| `name` | string [3..64] | yes |
| `description` | string [0..1000] | yes |
| `version` | string [1..32] | yes |
| `status` | active / inactive | yes |
| `config_version` | integer [1..2147483647] or null | yes |
| `developer_user_ids` | array<uuid (v7)> [1..20] | yes |
| `moderator_user_ids` | array<uuid (v7)> [1..20] | yes |
| `revision` | integer [1..2147483647] | yes |

### PackageConfig

| Field | Type / constraint | Required |
|---|---|---|
| `package_id` | uuid (v7) | yes |
| `config_version` | integer [1..2147483647] | yes |
| `definition` | PackageConfigInput | yes |

### PackageConfigInput

| Field | Type / constraint | Required |
|---|---|---|
| `stats` | array<StatDefinition> [1..32] | yes |
| `bonuses` | array<BonusRule> [0..32] | yes |
| `care_actions` | array<CareRule> [1..32] | yes |
| `daily_currency_cap` | integer [0..1000000] | yes |
| `starter` | Starter | yes |
| `assets` | array<Asset> [1..100] | yes |

### PackageConfigWrite

| Field | Type / constraint | Required |
|---|---|---|
| `expected_package_revision` | integer [1..2147483647] | yes |
| `definition` | PackageConfigInput | yes |

### PackageEdit

| Field | Type / constraint | Required |
|---|---|---|
| `name` | string [3..64] | yes |
| `description` | string [0..1000] | yes |
| `version` | string [1..32] | yes |
| `status` | active / inactive | yes |
| `developer_user_ids` | array<uuid (v7)> [1..20] | yes |
| `moderator_user_ids` | array<uuid (v7)> [1..20] | yes |

### PackageInput

| Field | Type / constraint | Required |
|---|---|---|
| `name` | string [3..64] | yes |
| `description` | string [0..1000] | yes |
| `version` | string [1..32] | yes |
| `developer_user_ids` | array<uuid (v7)> [1..20] | yes |
| `moderator_user_ids` | array<uuid (v7)> [1..20] | yes |

### PackageMember

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `membership_version` | integer [1..2147483647] | yes |

### PackageMemberPage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<PackageMember> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### PackagePage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<Package> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### RegistryOccurrenceChangedEvent

| Field | Type / constraint | Required |
|---|---|---|
| `event_id` | uuid (v7) | yes |
| `event_type` | "registry.occurrence_changed.v1" | yes |
| `occurred_at` | timestamp (ISO 8601 UTC) | yes |
| `producer` | "package-registry" | yes |
| `correlation_id` | uuid (v7) | yes |
| `data` | Occurrence | yes |

### Starter

| Field | Type / constraint | Required |
|---|---|---|
| `name` | string [1..64] | yes |
| `combat_type` | FLAME / NATURE / EARTH / ELECTRIC / WATER / SHADOW | yes |
| `sprite_ref` | string [1..512] | yes |
| `initial_stats` | map<string, ['number', 'string', 'boolean']> (bounded by schema) | yes |

### StarterConfig

| Field | Type / constraint | Required |
|---|---|---|
| `package_id` | uuid (v7) | yes |
| `config_version` | integer [1..2147483647] | yes |
| `starter` | Starter | yes |

### StatDefinition

| Field | Type / constraint | Required |
|---|---|---|
| `key` | string [1..64] | yes |
| `value_type` | NUMBER / STRING / BOOLEAN | yes |
| `minimum` | number [-1000000..1000000] or null | yes |
| `maximum` | number [-1000000..1000000] or null | yes |
| `allowed_strings` | array<string [1..64]> [0..50] or null | yes |

### StatDefinitions

| Field | Type / constraint | Required |
|---|---|---|
| `package_id` | uuid (v7) | yes |
| `config_version` | integer [1..2147483647] | yes |
| `stats` | array<StatDefinition> [1..32] | yes |
| `care_actions` | array<CareRule> [1..32] | yes |

## Map

### LocationInput

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `lat` | number [-90..90] | yes |
| `lng` | number [-180..180] | yes |
| `timestamp` | timestamp (ISO 8601 UTC) | yes |
| `accuracy_m` | number [0..100000] | no |

### LocationReceipt

| Field | Type / constraint | Required |
|---|---|---|
| `ok` | true | yes |
| `accepted` | boolean | yes |
| `reason` | ACCEPTED / DUPLICATE / STALE / OUT_OF_ORDER | yes |
| `current_timestamp` | date-time or null | yes |
| `expires_at` | date-time or null | yes |

### MapProximityDetectedEvent

| Field | Type / constraint | Required |
|---|---|---|
| `event_id` | uuid (v7) | yes |
| `event_type` | "map.proximity_detected.v1" | yes |
| `occurred_at` | timestamp (ISO 8601 UTC) | yes |
| `producer` | "map" | yes |
| `correlation_id` | uuid (v7) | yes |
| `data` | object {user_ids: array<uuid (v7)> [2..2], distance_m: number [0..6], encounter_id: uuid (v7), threshold_m: 6} | yes |

### Marker

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `lat` | number [-90..90] | yes |
| `lng` | number [-180..180] | yes |
| `timestamp` | timestamp (ISO 8601 UTC) | yes |
| `distance_m` | number [0..21000000] | yes |
| `relationship` | friend / enemy / stranger | yes |
| `accuracy_m` | number [0..100000] | no |

### Nearby

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `nearby` | array<Marker> [0..100] | yes |
| `retrieved_at` | timestamp (ISO 8601 UTC) | yes |
| `next_cursor` | string [1..2048] or null | yes |
| `partial` | boolean | yes |
| `partial_reason` | RELATIONSHIPS_UNAVAILABLE or null | yes |

## Monster Raid

### Leaderboard

| Field | Type / constraint | Required |
|---|---|---|
| `raid_id` | uuid (v7) | yes |
| `items` | array<LeaderboardItem> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |
| `retrieved_at` | timestamp (ISO 8601 UTC) | yes |
| `raid_version` | integer [1..2147483647] | yes |

### LeaderboardItem

| Field | Type / constraint | Required |
|---|---|---|
| `user_id` | uuid (v7) | yes |
| `tamagotchi_id` | uuid (v7) | yes |
| `damage_dealt` | integer [0..1000000000] | yes |
| `joined_at` | timestamp (ISO 8601 UTC) | yes |

### Raid

| Field | Type / constraint | Required |
|---|---|---|
| `raid_id` | uuid (v7) | yes |
| `guild_id` | uuid (v7) | yes |
| `boss_id` | uuid (v7) | yes |
| `occurrence_id` | uuid (v7) | yes |
| `boss` | RaidBoss | yes |
| `status` | ACTIVE / COMPLETED / FAILED / CANCELLED | yes |
| `started_at` | timestamp (ISO 8601 UTC) | yes |
| `expires_at` | timestamp (ISO 8601 UTC) | yes |
| `ended_at` | date-time or null | yes |
| `max_participants` | integer [1..100] | yes |
| `participant_count` | integer [0..100] | yes |
| `version` | integer [1..2147483647] | yes |
| `reward_status` | NOT_READY / PENDING / PARTIAL / DELIVERED / NOT_APPLICABLE / NEEDS_ATTENTION | yes |

### RaidAttack

| Field | Type / constraint | Required |
|---|---|---|
| `raid_id` | uuid (v7) | yes |
| `attacker_id` | uuid (v7) | yes |
| `damage_dealt` | integer [1..1000000000] | yes |
| `boss_hp_remaining` | integer [0..1000000000] | yes |
| `status` | ACTIVE / COMPLETED | yes |
| `raid_version` | integer [1..2147483647] | yes |
| `accepted_at` | timestamp (ISO 8601 UTC) | yes |
| `next_attack_at` | date-time or null | yes |

### RaidBoss

| Field | Type / constraint | Required |
|---|---|---|
| `name` | string [1..64] | yes |
| `max_hp` | integer [1..1000000000] | yes |
| `current_hp` | integer [0..1000000000] | yes |
| `weaknesses` | array<FLAME / NATURE / EARTH / ELECTRIC / WATER / SHADOW> [0..6] | yes |
| `resistances` | array<FLAME / NATURE / EARTH / ELECTRIC / WATER / SHADOW> [0..6] | yes |

### RaidCompletedEvent

| Field | Type / constraint | Required |
|---|---|---|
| `event_id` | uuid (v7) | yes |
| `event_type` | "raid.completed.v1" | yes |
| `occurred_at` | timestamp (ISO 8601 UTC) | yes |
| `producer` | "monster-raid" | yes |
| `correlation_id` | uuid (v7) | yes |
| `data` | object {raid_id: uuid (v7), guild_id: uuid (v7), outcome: VICTORY / DEFEAT / CANCELLED, status: COMPLETED / FAILED / CANCELLED, ended_at: date-time, reward_status: PENDING / NOT_APPLICABLE} | yes |

### RaidInput

| Field | Type / constraint | Required |
|---|---|---|
| `guild_id` | uuid (v7) | yes |
| `occurrence_id` | uuid (v7) | yes |

### RaidPage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<Raid> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### RaidStartedEvent

| Field | Type / constraint | Required |
|---|---|---|
| `event_id` | uuid (v7) | yes |
| `event_type` | "raid.started.v1" | yes |
| `occurred_at` | timestamp (ISO 8601 UTC) | yes |
| `producer` | "monster-raid" | yes |
| `correlation_id` | uuid (v7) | yes |
| `data` | object {raid_id: uuid (v7), guild_id: uuid (v7), boss_name: string [1..64], recipient_user_ids: array<uuid (v7)> [1..100], started_at: date-time, expires_at: date-time} | yes |

## Notification

### Device

| Field | Type / constraint | Required |
|---|---|---|
| `id` | uuid (v7) | yes |
| `user_id` | uuid (v7) | yes |
| `platform` | ANDROID / IOS / WEB | yes |
| `package_id` | uuid (v7) | yes |
| `locale` | string [1..35] | yes |
| `registered_at` | timestamp (ISO 8601 UTC) | yes |

### DeviceInput

| Field | Type / constraint | Required |
|---|---|---|
| `fcm_token` | string [1..4096] | yes |
| `platform` | ANDROID / IOS / WEB | yes |
| `package_id` | uuid (v7) | yes |
| `locale` | string [1..35] | yes |

### DevicePage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<Device> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### Notification

| Field | Type / constraint | Required |
|---|---|---|
| `id` | uuid (v7) | yes |
| `user_id` | uuid (v7) | yes |
| `type` | FRIEND_REQUEST / PLAYER_NEARBY / BATTLE_REQUEST / TAMAGOTCHI_CAPTURED / GUILD_INVITATION / RAID_STARTED | yes |
| `event_id` | uuid (v7) | yes |
| `params` | map<string, ['string', 'number', 'boolean']> (bounded by schema) | yes |
| `created_at` | timestamp (ISO 8601 UTC) | yes |
| `read_at` | date-time or null | yes |
| `delivery_status` | PENDING / ACCEPTED_BY_PROVIDER / SUPPRESSED / NO_DEVICE / EXPIRED / FAILED | yes |

### NotificationPage

| Field | Type / constraint | Required |
|---|---|---|
| `items` | array<Notification> [0..100] | yes |
| `next_cursor` | string [1..2048] or null | yes |

### Preferences

| Field | Type / constraint | Required |
|---|---|---|
| `muted_categories` | array<FRIEND_REQUEST / PLAYER_NEARBY / BATTLE_REQUEST / TAMAGOTCHI_CAPTURED / GUILD_INVITATION / RAID_STARTED> [0..6] | yes |
| `version` | integer [1..2147483647] | yes |

### PreferencesInput

| Field | Type / constraint | Required |
|---|---|---|
| `muted_categories` | array<FRIEND_REQUEST / PLAYER_NEARBY / BATTLE_REQUEST / TAMAGOTCHI_CAPTURED / GUILD_INVITATION / RAID_STARTED> [0..6] | yes |

### ReadAllInput

| Field | Type / constraint | Required |
|---|---|---|
| `created_before` | timestamp (ISO 8601 UTC) | yes |

### ReadAllReceipt

| Field | Type / constraint | Required |
|---|---|---|
| `updated_count` | integer [0..9007199254740991] | yes |

### ReadInput

| Field | Type / constraint | Required |
|---|---|---|
| `read` | true | yes |
