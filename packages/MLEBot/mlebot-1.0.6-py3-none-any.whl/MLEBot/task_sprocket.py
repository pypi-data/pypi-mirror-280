#!/usr/bin/env python
""" Sprocket Periodic Task
# Author: irox_rl
# Purpose: Get MLE information hosted from sprocket for use in parsing sprocket_data
# Version 1.0.4
"""

from PyDiscoBot import err

# local imports #
from MLEBot.sprocket_data_link import SprocketDataLink

# non-local imports #
import datetime
import pickle


class Task_Sprocket:
    def __init__(self, master_bot):
        self.bot = master_bot
        self.league_update_flag = False
        self._members_link = SprocketDataLink(
            "https://f004.backblazeb2.com/file/sprocket-artifacts/public/data/members")
        self._player_stats_link = SprocketDataLink(
            "https://f004.backblazeb2.com/file/sprocket-artifacts/public/data/player_stats")
        self._players_link = SprocketDataLink(
            "https://f004.backblazeb2.com/file/sprocket-artifacts/public/data/players")
        self._scrim_stats_link = SprocketDataLink(
            "https://f004.backblazeb2.com/file/sprocket-artifacts/public/data/scrim_stats")
        self._teams_link = SprocketDataLink("https://f004.backblazeb2.com/file/sprocket-artifacts/public/data/teams")
        self._fixtures_link = SprocketDataLink(
            "https://f004.backblazeb2.com/file/sprocket-artifacts/public/data/schedules/fixtures")
        self._match_groups_link = SprocketDataLink(
            "https://f004.backblazeb2.com/file/sprocket-artifacts/public/data/schedules/match_groups")
        self._matches_link = SprocketDataLink(
            "https://f004.backblazeb2.com/file/sprocket-artifacts/public/data/schedules/matches")
        self._trackers_link = SprocketDataLink(
            "https://f004.backblazeb2.com/file/sprocket-artifacts/public/data/trackers")

        self.on_updated = []

        self._file_name = 'sprocket_data.pickle'
        self._loaded = False
        self._last_time_ran: datetime.datetime | None = None
        self._next_run_time: datetime.datetime | None = None

    @property
    def all_links_loaded(self) -> bool:
        if (self._members_link.last_time_updated and
                self._player_stats_link.last_time_updated and
                self._players_link.last_time_updated and
                self._scrim_stats_link.last_time_updated and
                self._teams_link.last_time_updated and
                self._fixtures_link.last_time_updated and
                self._match_groups_link.last_time_updated and
                self._matches_link.last_time_updated and
                self._trackers_link.last_time_updated):
            return True
        return False

    @property
    def data(self) -> {}:
        return {'sprocket_members': self._members_link.json_data,
                'sprocket_player_stats': self._player_stats_link.json_data,
                'sprocket_players': self._players_link.json_data,
                'sprocket_scrim_stats': self._scrim_stats_link.json_data,
                'sprocket_teams': self._teams_link.json_data,
                'sprocket_fixtures': self._fixtures_link.json_data,
                'sprocket_match_groups': self._match_groups_link.json_data,
                'sprocket_matches': self._matches_link.json_data,
                'sprocket_trackers': self._trackers_link.json_data,
                }

    @property
    def members_link(self):
        return self._player_stats_link

    @property
    def player_stats_link(self):
        return self._player_stats_link

    @property
    def players_link(self):
        return self._players_link

    @property
    def scrim_stats_link(self):
        return self._scrim_stats_link

    @property
    def teams_link(self):
        return self._teams_link

    @property
    def trackers_link(self):
        return self._trackers_link

    @property
    def fixtures_link(self):
        return self._fixtures_link

    @property
    def match_groups_link(self):
        return self._match_groups_link

    @property
    def matches_link(self):
        return self._matches_link

    @property
    def ready_to_update(self) -> bool:
        if self._next_run_time <= datetime.datetime.now():
            return True
        return False

    def __get_next_run_time__(self):
        self._last_time_ran = datetime.datetime.now()
        if self._last_time_ran.hour < 6:
            self._next_run_time = self._last_time_ran + datetime.timedelta(hours=(6 - self._last_time_ran.hour),
                                                                           minutes=(0 - self._last_time_ran.minute),
                                                                           seconds=(0 - self._last_time_ran.second))
            return
        if self._last_time_ran.hour < 12:
            self._next_run_time = self._last_time_ran + datetime.timedelta(hours=(12 - self._last_time_ran.hour),
                                                                           minutes=(0 - self._last_time_ran.minute),
                                                                           seconds=(0 - self._last_time_ran.second))
            return
        if self._last_time_ran.hour < 18:
            self._next_run_time = self._last_time_ran + datetime.timedelta(hours=(18 - self._last_time_ran.hour),
                                                                           minutes=(0 - self._last_time_ran.minute),
                                                                           seconds=(0 - self._last_time_ran.second))
            return
        self._next_run_time = self._last_time_ran + datetime.timedelta(hours=(0 - self._last_time_ran.hour),
                                                                       minutes=(0 - self._last_time_ran.minute),
                                                                       seconds=(0 - self._last_time_ran.second), days=1)
        return

    def __reset_link_flags__(self):
        self._members_link.updated_flag = False
        self._player_stats_link.updated_flag = False
        self._players_link.updated_flag = False
        self._scrim_stats_link.updated_flag = False
        self._teams_link.updated_flag = False
        self._fixtures_link.updated_flag = False
        self._match_groups_link.updated_flag = False
        self._matches_link.updated_flag = False
        self.trackers_link.updated_flag = False

    def load(self):
        try:
            with open(self._file_name, 'rb') as f:  # Open save file
                data = pickle.load(f)
                self._members_link.decompress(data[0])
                self._player_stats_link.decompress(data[1])
                self._players_link.decompress(data[2])
                self._scrim_stats_link.decompress(data[3])
                self._teams_link.decompress(data[4])
                self._fixtures_link.decompress(data[5])
                self._match_groups_link.decompress(data[6])
                self._matches_link.decompress(data[7])
                self._trackers_link.decompress(data[8])
                self._last_time_ran = data[9]['last_time_ran']
                self._next_run_time = data[9]['next_run_time']
        except (KeyError, FileNotFoundError, EOFError) as e:
            self._next_run_time = datetime.datetime.now()
        finally:
            self._loaded = True

    def reset(self):
        self._next_run_time = datetime.datetime.now()

    async def run(self):
        if not self._loaded:
            self.load()
        if self.ready_to_update:
            await self._members_link.data()
            await self._player_stats_link.data()
            await self._players_link.data()
            await self._scrim_stats_link.data()
            await self._teams_link.data()
            await self._fixtures_link.data()
            await self._match_groups_link.data()
            await self._matches_link.data()
            await self._trackers_link.data()
        else:
            return
        self.__get_next_run_time__()
        self.save()
        for callback in self.on_updated:
            await callback({
                'sprocket_members': self._members_link.json_data,
                'sprocket_player_stats': self._player_stats_link.json_data,
                'sprocket_players': self._players_link.json_data,
                'sprocket_scrim_stats': self._scrim_stats_link.json_data,
                'sprocket_teams': self._teams_link.json_data,
                'sprocket_fixtures': self._fixtures_link.json_data,
                'sprocket_match_groups': self._match_groups_link.json_data,
                'sprocket_matches': self._matches_link.json_data,
                'sprocket_trackers': self._trackers_link.json_data,
            })
        await err('sprocket server links updated.')

    def save(self):
        with open(self._file_name, 'wb') as f:
            pickle.dump([self._members_link.compress(),
                         self._player_stats_link.compress(),
                         self._players_link.compress(),
                         self._scrim_stats_link.compress(),
                         self._teams_link.compress(),
                         self._fixtures_link.compress(),
                         self._match_groups_link.compress(),
                         self._matches_link.compress(),
                         self._trackers_link.compress(),
                         {
                             'last_time_ran': self._last_time_ran,
                             'next_run_time': self._next_run_time,
                         }], f)
