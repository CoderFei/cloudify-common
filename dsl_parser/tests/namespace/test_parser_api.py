from dsl_parser.tests.abstract_test_parser import AbstractTestParser


class TestNamespaceImport(AbstractTestParser):

    def test_node_type_import(self):
        yaml = self.BASIC_VERSION_SECTION_DSL_1_3 + """
node_types:
  test_type:
    properties:
      prop1:
        default: value"""
        bottom_file_name = self.make_yaml_file(yaml)

        top_level_yaml = self.BASIC_VERSION_SECTION_DSL_1_3 + """
node_templates:
    test_node:
        type: test::test_type
imports:
    -   {0}::{1}
""".format('test', bottom_file_name)

        result = self.parse(top_level_yaml)

    def test_merging_node_type_import(self):
        # TODO: deal with merging
        yaml = self.BASIC_VERSION_SECTION_DSL_1_3 + """
node_types:
  test_type:
    properties:
      prop1:
        default: value"""
        bottom_file_name = self.make_yaml_file(yaml)

        top_level_yaml = self.BASIC_VERSION_SECTION_DSL_1_3 + """
node_types:
  test_type2:
    properties:
      prop1:
        default: value

node_templates:
    test_node:
        type: test::test_type
    test_node2:
        type: test_type2
imports:
    -   {0}::{1}
""".format('test', bottom_file_name)

        result = self.parse(top_level_yaml)


class TestNamespacedDataTypes(AbstractTestParser):
    def test_namespaced_date_types(self):
        yaml = self.BASIC_VERSION_SECTION_DSL_1_3 + """
data_types:
    test_type:
        properties:
            test: {}
    pair_of_pairs_type:
        properties:
            test_prop:
                type: test_type
"""
        bottom_file_name = self.make_yaml_file(yaml)

        top_level_yaml = self.BASIC_VERSION_SECTION_DSL_1_3 + self.MINIMAL_BLUEPRINT + """
imports:
    -   {0}::{1}
""".format('test', bottom_file_name)

        self.parse(top_level_yaml)

    def test_implicit_default_value(self):
        pass

    def test_nested_defaults(self):
        pass

    def test_imports_merging(self):
        file1 = """
data_types:
    data1:
        properties:
            prop1:
                default: value1
"""
        import_path = self.make_yaml_file(file1)
        yaml = """
imports:
  - {0}::{1}
data_types:
    data2:
        properties:
            prop2:
                default: value2
node_types:
    type:
        properties:
            prop1:
                type: data1
            prop2:
                type: data2
node_templates:
    node:
        type: type
""".format('test', import_path)
        properties = self.parse_1_3(yaml)['nodes'][0]['properties']
        self.assertEqual(properties['prop1']['prop1'], 'value1')
        self.assertEqual(properties['prop2']['prop2'], 'value2')

    def test_nested_merge_with_inheritance(self):
        pass

    def test_complex_nested_merging(self):
        pass

    def test_subtype_override_field_type(self):
        pass

    def test_derives(self):
        pass