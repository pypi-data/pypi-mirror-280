use std::path::{Path, PathBuf};

use pyo3::prelude::*;

use segul::{
    handler::align::concat::ConcatHandler,
    helper::{
        finder::SeqFileFinder,
        types::{DataType, InputFmt, OutputFmt, PartitionFmt},
    },
};

use super::{DATA_TYPE_ERR, INPUT_FMT_ERR, OUTPUT_FMT_ERR, PARTITION_FMT_ERR};

#[pyclass]
pub(crate) struct AlignmentConcatenation {
    input_files: Vec<PathBuf>,
    input_fmt: InputFmt,
    datatype: DataType,
    output_dir: PathBuf,
    output_fmt: OutputFmt,
    partition_fmt: PartitionFmt,
    output_prefix: Option<String>,
}

#[pymethods]
impl AlignmentConcatenation {
    #[new]
    pub(crate) fn new(
        input_fmt: &str,
        datatype: &str,
        output_dir: &str,
        output_fmt: &str,
        partition_fmt: &str,
        output_prefix: Option<String>,
    ) -> Self {
        Self {
            input_files: Vec::new(),
            input_fmt: input_fmt.parse::<InputFmt>().expect(INPUT_FMT_ERR),
            datatype: datatype.parse::<DataType>().expect(DATA_TYPE_ERR),
            output_dir: PathBuf::from(output_dir),
            output_fmt: output_fmt.parse::<OutputFmt>().expect(OUTPUT_FMT_ERR),
            partition_fmt: partition_fmt
                .parse::<PartitionFmt>()
                .expect(PARTITION_FMT_ERR),
            output_prefix,
        }
    }

    pub(crate) fn from_files(&mut self, input_files: Vec<String>) {
        self.input_files = input_files.iter().map(PathBuf::from).collect();
        self.concat_alignments();
    }

    pub(crate) fn from_dir(&mut self, input_dir: &str) {
        let input_dir = Path::new(input_dir);
        self.input_files = SeqFileFinder::new(input_dir).find(&self.input_fmt);
        self.concat_alignments();
    }

    fn concat_alignments(&mut self) {
        let prefix = match &self.output_prefix {
            Some(prefix) => PathBuf::from(prefix),
            None => self.output_dir.clone(),
        };
        let mut handle = ConcatHandler::new(
            &self.input_fmt,
            &self.output_dir,
            &self.output_fmt,
            &self.partition_fmt,
            &prefix,
        );
        handle.concat_alignment(&mut self.input_files, &self.datatype);
    }
}
