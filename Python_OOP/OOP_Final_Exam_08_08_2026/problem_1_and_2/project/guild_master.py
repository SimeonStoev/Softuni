from project.guild_halls.combat_hall import CombatHall
from project.guild_halls.magic_tower import MagicTower
from project.guild_members.mage import Mage
from project.guild_members.warrior import Warrior
from project.guild_halls.base_guild_hall import BaseGuildHall


class GuildMaster:
    MEMBERS = {"Warrior": Warrior, "Mage": Mage}
    GUILD_HALLS = {"CombatHall": CombatHall, "MagicTower": MagicTower}

    def __init__(self):
        self.members = []
        self.guild_halls = []

    def __is_member_type_valid(self, member_type: str):
        return member_type in GuildMaster.MEMBERS

    def __is_member_with_same_tag_exists(self, member_tag: str):
        return any(member.tag == member_tag for member in self.members)

    def __create_member(self, member_type: str, member_tag: str, member_gold: int):
        return GuildMaster.MEMBERS[member_type](member_tag, member_gold)

    def __is_guild_hall_type_valid(self, guild_hall_type: str):
        return guild_hall_type in GuildMaster.GUILD_HALLS

    def __is_guild_hall_with_same_alias_exists(self, guild_hall_alias: str):
        return any(hall.alias == guild_hall_alias for hall in self.guild_halls)

    def __create_guild_hall(self, guild_hall_type: str, guild_hall_alias: str):
        return GuildMaster.GUILD_HALLS[guild_hall_type](guild_hall_alias)

    def __get_guild_hall_by_alias(self, guild_hall_alias: str):
        for guild_hall in self.guild_halls:
            if guild_hall.alias == guild_hall_alias:
                return guild_hall
        return None

    def __get_member_by_type(self, member_type: str):
        return next((member for member in self.members if member.__class__.__name__ == member_type), None)

    def __update_members_gold_in_guild_halls(self, min_skill_level_value: int):
        for guild_hall in self.guild_halls:
            guild_hall.increase_gold(min_skill_level_value)

    def add_member(self, member_type: str, member_tag: str, member_gold: int):
        if not self.__is_member_type_valid(member_type):
            raise ValueError("Invalid member type!")

        if self.__is_member_with_same_tag_exists(member_tag):
            raise ValueError(f"{member_tag} has already been added!")

        new_member = self.__create_member(member_type, member_tag, member_gold)
        self.members.append(new_member)
        return f"{member_tag} is successfully added as {member_type}."

    def add_guild_hall(self, guild_hall_type: str, guild_hall_alias: str):
        if not self.__is_guild_hall_type_valid(guild_hall_type):
            raise ValueError("Invalid guild hall type!")

        if self.__is_guild_hall_with_same_alias_exists(guild_hall_alias):
            raise ValueError(f"{guild_hall_alias} has already been added!")

        new_guild_hall = self.__create_guild_hall(guild_hall_type, guild_hall_alias)
        self.guild_halls.append(new_guild_hall)
        return f"{guild_hall_alias} is successfully added as a {guild_hall_type}."

    def assign_member(self, guild_hall_alias: str, member_type: str):
        guild_hall = self.__get_guild_hall_by_alias(guild_hall_alias)
        member = self.__get_member_by_type(member_type)
        if not guild_hall:
            raise ValueError(f"Guild hall {guild_hall_alias} does not exist!")

        if not member:
            raise ValueError("No available members of the type!")

        if len(guild_hall.members) == guild_hall.max_member_count:
            return "Maximum member count reached. Assignment is impossible."

        self.members.remove(member)
        guild_hall.members.append(member)
        return f"{member.tag} was assigned to {guild_hall_alias}."

    def practice_members(self, guild_hall: BaseGuildHall, sessions_number: int):
        for _ in range(sessions_number):
            for member in guild_hall.members:
                member.practice()

        total_skill_level = sum(member.skill_level for member in guild_hall.members)
        return f"{guild_hall.alias} members have {total_skill_level} total skill level after {sessions_number} practice session/s."

    def unassign_member(self, guild_hall: BaseGuildHall, member_tag: str):
        member = next((member for member in guild_hall.members if member.tag == member_tag and member.skill_level < 10),
                      None)
        if not member:
            return "The unassignment process was canceled."

        guild_hall.members.remove(member)
        self.members.append(member)
        return f"Unassigned member {member_tag}."

    def guild_update(self, min_skill_level_value: int):
        self.__update_members_gold_in_guild_halls(min_skill_level_value)

        sorted_guild_halls = sorted(self.guild_halls, key=lambda x: (-len(x.members), x.alias))

        lines = ["<<<Guild Updated Status>>>", f"Unassigned members count: {len(self.members)}",
                 f"Guild halls count: {len(self.guild_halls)}"]

        for guild_hall in sorted_guild_halls:
            lines.append(f">>>{guild_hall.status()}")

        return "\n".join(lines).strip()
