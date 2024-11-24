import json
import csv
import xml.etree.ElementTree as ET


class BookAdapter:
    """
    Adapter for converting book data from various formats into a standard dictionary format.
    """

    @staticmethod
    def from_json(json_data):
        """
        Converts JSON data to the standard format.
        :param json_data: str, JSON string containing book data
        :return: dict, standardized book data
        """
        data = json.loads(json_data)
        return {"title": data["title"], "author": data["author"], "year": int(data["year"])}

    @staticmethod
    def from_csv(csv_data):
        """
        Converts CSV data to the standard format.
        :param csv_data: str, CSV string containing book data
        :return: dict, standardized book data
        """
        reader = csv.reader(csv_data.splitlines())
        header = next(reader)  
        row = next(reader)  
        return dict(zip(header, row))

    @staticmethod
    def from_xml(xml_data):
        """
        Converts XML data to the standard format.
        :param xml_data: str, XML string containing book data
        :return: dict, standardized book data
        """
        root = ET.fromstring(xml_data)
        return {
            "title": root.find("title").text,
            "author": root.find("author").text,
            "year": int(root.find("year").text),
        }
