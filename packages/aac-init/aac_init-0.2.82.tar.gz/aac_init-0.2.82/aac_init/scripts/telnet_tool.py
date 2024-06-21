# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Wang Xiao <xiawang3@cisco.com>


import asyncio
import telnetlib3
import logging

from telnetlib3 import TelnetReaderUnicode, TelnetWriterUnicode
from aac_init.scripts.logging_tool import setup_logging


logger = setup_logging()


async def open_connection(host, port):
    try:
        reader, writer = await telnetlib3.open_connection(host, port)
        logger.info(f"connect success: {host}:{port}")
        return reader, writer
    except Exception as e:
        logger.error(
            '[{}:{}] connected failed!'
            .format(host, port)
        )
        logger.error(f"[{host}:{port}]:Exception details: {e}")
        return None, None


class TelnetClient:
    def __init__(
            self,
            telnet_ip,
            telnet_port,
            telnet_username,
            telnet_password
    ):
        self.reader = None
        self.writer = None
        self.host_ip = telnet_ip
        self.port = telnet_port
        self.username = telnet_username
        self.password = telnet_password

    async def read_until(self, match, timeout=None):
        if self.reader:
            try:
                return await asyncio.wait_for(self.reader.readuntil(match), timeout)
            except asyncio.TimeoutError:
                return False
            except Exception as e:
                return False
        else:
            return False

    async def async_login_host(self):
        logger.info(
            "Start Telnet connection validation for {}:{}".format(
                self.host_ip, self.port
            )
        )
        self.reader, self.writer = await open_connection(
            self.host_ip, self.port
        )
        if not self.reader:
            return False

        self.writer.write('\n')

        prompt_str = await self.read_until(b'#', timeout=10)
        if prompt_str:
            logger.info(
                "[{}:{}] login success without username and pwd. prompt: {}".format(
                    self.host_ip, self.port, prompt_str.decode()
                )
            )
            return True
        logger.info(
            "[{}:{}] login failed without username and pwd.".format(
                self.host_ip, self.port
            )
        )

        login_str = await self.read_until(b'login: ', timeout=10)
        if not login_str:
            logger.info("[{}:{}] no login word".format(self.host_ip, self.port))
            return False

        try:
            host_name = login_str.decode('US-ASCII').split('\r\n')[-1].split(' ')[0].strip()
        except Exception as e:
            logger.warning(
                "[{}:{}] get host name failed".format(self.host_ip, self.port)
            )

        self.writer.write(self.username + '\n')

        pwd_prompt = await self.read_until(b'Password:', timeout=10)
        if not pwd_prompt:
            logger.info("[{}:{}] no password prompt".format(self.host_ip, self.port))
            return False

        self.writer.write(self.password + '\n')

        prompt_str = await self.read_until(b'#', timeout=10)
        if not prompt_str:
            logger.info("[{}:{}] no #".format(self.host_ip, self.port))
            return False

        logger.info(
                "[{}:{}] login success. prompt: [{}]".format(
                    self.host_ip, self.port, prompt_str.decode()
                )
            )
        return True

    async def async_login_host_with_info(self):
        result = await self.async_login_host()
        return result, self.host_ip, self.port

    def login_host(self):
        return asyncio.run(self.async_login_host())


async def batch_check_host(devices, batch_size=10):
    results = []
    if len(devices) <= batch_size:
        tasks = [TelnetClient(host, port, username, password).async_login_host_with_info() for
                 host, port, username, password in devices]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

    for i in range(0, len(devices), batch_size):
        tasks = [TelnetClient(host, port, username, password).async_login_host_with_info() for
                 host, port, username, password in devices[i: i + batch_size]]
        results += await asyncio.gather(*tasks, return_exceptions=True)
    return results

