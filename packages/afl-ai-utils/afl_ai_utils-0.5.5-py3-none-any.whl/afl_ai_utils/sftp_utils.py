import io
import paramiko
import pandas as pd
from io import StringIO
import traceback
import logging
from logging_utils import setup_logger, clean_up_logger

logger = setup_logger("afl_ai_utils", log_file="afl_ai_utils.log", level=logging.DEBUG)


class SFTPUtils:
    def __init__(self, host, username, password, port):
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def read_from_sftp_server(self, file_path):
        transport = paramiko.Transport(self.username, int(self.port))
        transport.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        df = None
        if sftp.stat(file_path):
            logger.info(f"Reading the file from SFTP server: {file_path}")
            with sftp.file(file_path, 'r') as file:
                buffer = io.StringIO(file.read().decode())
            df = pd.read_csv(buffer)
            logger.info(f"File read successfully. Number of rows: {len(df)}")
        else:
            logger.info(f"File {file_path} doesn't exists on SFTP server: {file_path}")

        sftp.close()
        transport.close()
        return df

    def write_to_sftp_server(self, remote_path: str, dataframe: pd.DataFrame):
        try:
            csv_string = dataframe.to_csv(index=False)
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(self.host, self.port, self.username, self.password)
            sftp = ssh_client.open_sftp()
            csv_buffer = StringIO(csv_string)
            with sftp.file(remote_path, "w") as file:
                file.write(csv_buffer.getvalue())
            sftp.close()
            ssh_client.close()
            logger.info("Data written successfully to", remote_path)
        except Exception as e:
            print("Error:", str(e), "---> ", traceback.format_exc())


clean_up_logger(logger=logger)
